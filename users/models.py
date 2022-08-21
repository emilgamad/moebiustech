from django.db import models
from app.models import Product, Choice


class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=200)
    verified = models.BooleanField(False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


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

    def __str__(self):
        if self.company_name:
            return "{}".format(self.company_name)
        else:
            return "{}".format(self.company_person)


class Reviews(models.Model):
    pass
