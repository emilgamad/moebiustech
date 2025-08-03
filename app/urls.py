
"""
URL routing for the app module.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.detail, name="detail"),
    path("<int:product_id>/filter/", views.filter, name="filter"),
    path("<int:product_id>/question/", views.question, name="question"),
]
