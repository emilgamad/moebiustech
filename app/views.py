
"""
View functions for the app module.
"""

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Question, Product, Choice

def index(request):
    """
    Display the index page with the latest products.
    """
    latest_product_list = Product.objects.all()
    context = {"latest_product_list": latest_product_list}
    return render(request, "app/index.html", context)

def detail(request, product_id):
    """
    Display the detail page for a specific product.
    """
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product}
    return render(request, "app/detail.html", context)

def filter(request, product_id):
    """
    Display the filter page for questions related to a product.
    """
    questions = get_list_or_404(Question, product_id=product_id)
    context = {"questions": questions}
    return render(request, "app/filter.html", context)

def question(request, question_id):
    """
    Display the choices for a specific question.
    """
    choices = get_list_or_404(Choice, question_id=question_id)
    context = {"choices": choices}
    return render(request, "app/questions.html", context)
