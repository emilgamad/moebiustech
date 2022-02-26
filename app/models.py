from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0) #conversion of different currencies?
    price_with_vat = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0) #conversion of different currencies?
    price_with_vat = models.DecimalField(max_digits=6, decimal_places=2, default=0)

class Details(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    in_stock_online = models.BooleanField(default=True)
    in_stock_physical = models.BooleanField(default=True)
    brief_description = models.TextField()
    original_description = models.TextField()
    technical_description = models.TextField()
    delivery_time = models.DateField()
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0) #conversion of different currencies?
    class Delivery(models.TextChoices):
        POSTAL_DELIVERY = 'PO', _('Postal Delivery')
        COLLECTION_AT_STORE = 'CAS', _('Collection at Store')
        ASSOCIATED_DISTRIBUTION_POINT = 'ADP', _('Assosciated Distribution Point')
    return_information = models.TextField()
    contact_infomation = models.TextField()
    help_information = models.TextField()
    product_warranty = models.TextField()

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    #images - raw file vs set with aws, possible django storages

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    comment = models.TextField()
    rating = models.IntegerField(default=0)

class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['product']

    def __str__(self):
        return "{} - {}".format(self.product, self.question_text)
    

class Choice(models.Model):
    question = models.ManyToManyField(Question)
    choice_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.choice_text)


class Searche(models.Model):
    zip_code = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    question = models.ManyToManyField(Question)
    choice = models.ManyToManyField(Choice)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=200)
    project_location = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.client, self.service)



