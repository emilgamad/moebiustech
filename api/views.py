from django.shortcuts import render, redirect
from app.models import Product, Question, Choice, Searche
from users.models import Contractor, Client
from .serializers import ProductSerializer, QuestionSerializer, ChoiceSerializer, SearcheSerializer, ClientSerializer, ContractorSerializer
from rest_framework import viewsets


class Product(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Question(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class Choice(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class Searche(viewsets.ModelViewSet):
    queryset = Searche.objects.all()
    serializer_class = SearcheSerializer

class Contractor(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class Client(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer