from django.db import models
from app.models import Product


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
    logo = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    product = models.ManyToManyField(Product)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Reviews(models.Model):
    pass
