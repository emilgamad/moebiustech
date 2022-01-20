from django.contrib import admin

from .models import Product,Question,Choice,Searche

admin.site.register(Product)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Searche)