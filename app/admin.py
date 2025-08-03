
"""
Admin configuration for the app module.
"""

from django.contrib import admin

from .models import Product, Question, Choice, Searche, Result, Contractor

admin.site.register(Product)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Searche)
admin.site.register(Result)
admin.site.register(Contractor)
