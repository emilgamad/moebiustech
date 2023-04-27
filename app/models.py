from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from geopy import distance
from geopy.geocoders import Nominatim
import logging

locator = Nominatim(user_agent="myGeocoder")


class Product(models.Model):
    position = models.IntegerField(default=0)
    service_slug = models.SlugField(max_length=200, blank=True)
    service_label = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    # --------------------------#
    create_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0
    )  # conversion of different currencies?
    price_with_vat = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.service_label} - {self.id}"

    def save(self, *args, **kwargs):
        if Product.objects.last() is None:
            last_position = 0
        else:
            last_position = Product.objects.last().position
        self.position = last_position + 1
        self.service_slug = slugify(self.service_label)
        super().save(*args, **kwargs)


class Choice(models.Model):
    position = models.IntegerField(default=0)
    value = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.label)

    def save(self, *args, **kwargs):
        if Choice.objects.last() is None:
            last_position = 0
        else:
            last_position = Choice.objects.last().position
        self.position = last_position + 1
        self.value = slugify(self.label)
        super().save(*args, **kwargs)


class Question(models.Model):
    QUESTION_TYPE = [
        ("RadioQuestion", "Radio Question"),
        ("CheckboxQuestion", "Checkbox Question"),
        ("DropdownQuestion", "Dropdown Question"),
    ]
    position = models.IntegerField(default=0)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE)
    question_label = models.CharField(max_length=200)
    question_slug = models.SlugField(max_length=200, blank=True)
    is_required = models.BooleanField(default=False)
    is_multiple = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    choices = models.ManyToManyField(Choice, blank=True)
    # --------------------------#
    create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ["product"]

    def __str__(self):
        return "{} - {}".format(self.product, self.question_label)

    def save(self, *args, **kwargs):
        self.question_slug = slugify(self.question_label)
        super().save(*args, **kwargs)


class Contractor(models.Model):
    product = models.ManyToManyField(Product)
    experties = models.ManyToManyField(Choice)
    company_name = models.CharField(max_length=200, blank=True)
    company_person = models.CharField(max_length=200, blank=True)
    field = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=500, blank=True)
    zip_code = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    about = models.CharField(max_length=500, blank=True)
    logo = models.ImageField(blank=True)
    website = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    internal_notes = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    service_area = models.CharField(max_length=200, blank=True)
    location_longitude = models.FloatField(null=True, blank=True)
    location_langitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.company_name:
            return "{}".format(self.company_name)
        else:
            return "{}".format(self.company_person)


class Result(models.Model):
    nearby_contractors = models.ManyToManyField(
        Contractor, related_name="nearby_contractors"
    )
    oor_contractors = models.ManyToManyField(Contractor, related_name="oor_contractors")


class Searche(models.Model):
    location_longitude = models.FloatField()
    location_langitude = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    answer = models.JSONField(null=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    contact_person = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    result = models.ForeignKey(Result, on_delete=models.SET_NULL, null=True)
    # ------------#
    project_location = models.CharField(max_length=200, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        self.project_location = locator.reverse(
            f"{self.location_longitude},{self.location_langitude}",
            zoom=18
        ).address
        if self.answer:
            # parse input
            question_id = self.answer[0]["question_id"]
            choices_id = self.answer[0]["choices"][0]
            question = Question.objects.get(id=question_id)
            choice = Choice.objects.get(id=choices_id)
            product = Product.objects.get(id=question.product.id)

            search_result = Result()
            search_result.save()

            # filter nearby contractors
            nearby_contractors = Contractor.objects.filter(
                product__id=product.id,
                experties__id=choice.id,
                service_area__in=self.project_location.split(", "),
            )[:5]

            # filter oor contractors
            matched_contractors = list(
                Contractor.objects.filter(
                    product__id=product.id, 
                    experties__id=choice.id,
                )[:5]
            )

            for each in nearby_contractors:
                search_result.nearby_contractors.add(each)
                matched_contractors.remove(each)

            for each in matched_contractors:
                search_result.oor_contractors.add(each)

            self.result = search_result
        super().save(*args, **kwargs)

    def __str__(self):
        if self.answer:
            question_id = self.answer[0]["question_id"]
            choices_id = self.answer[0]["choices"][0]
            question = Question.objects.get(id=question_id)
            choice = Choice.objects.get(id=choices_id)

        return "{} - {}".format(question, choice)


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0
    )  # conversion of different currencies?
    price_with_vat = models.DecimalField(max_digits=6, decimal_places=2, default=0)


class Details(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    in_stock_online = models.BooleanField(default=True)
    in_stock_physical = models.BooleanField(default=True)
    brief_description = models.TextField()
    original_description = models.TextField()
    technical_description = models.TextField()
    delivery_time = models.DateField()
    shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=0
    )  # conversion of different currencies?

    class Delivery(models.TextChoices):
        POSTAL_DELIVERY = "PO", _("Postal Delivery")
        COLLECTION_AT_STORE = "CAS", _("Collection at Store")
        ASSOCIATED_DISTRIBUTION_POINT = "ADP", _("Assosciated Distribution Point")

    return_information = models.TextField()
    contact_infomation = models.TextField()
    help_information = models.TextField()
    product_warranty = models.TextField()


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    # images - raw file vs set with aws, possible django storages


class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    rating = models.IntegerField(default=0)
