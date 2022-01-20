from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    question_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.product, self.question_text)
    

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.SET_NULL,null=True)
    choice_text = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.question, self.choice_text)


class Searche(models.Model):
    zip_code = models.CharField(max_length=200)
    product = models.ForeignKey( Product,on_delete=models.SET_NULL,null=True)
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



