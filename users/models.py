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
    experties = models.ManyToManyField(Choice)
    product = models.ManyToManyField(Product)
    company_name = models.CharField(max_length=200)
    company_person = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    zip_code = models.CharField(max_length=200)
    email = models.EmailField(Choice)
    about = models.CharField(max_length=500)
    logo = models.ImageField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "{}".format(self.company_name)


class Reviews(models.Model):
    pass
