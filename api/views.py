from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product, Question as testq, Choice, Searche, Service
from users.models import Contractor, Client
from .serializers import ProductSerializer, QuestionSerializer, ChoiceSerializer, \
    SearcheSerializer, ClientSerializer, ContractorSerializer, ServiceSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response


class Product(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Question(ReadOnlyModelViewSet):
    queryset = testq.objects.all()
    serializer_class = QuestionSerializer

class Choice(ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class Service(ReadOnlyModelViewSet):
    pass
    #queryset = Question.objects.all()
    #queryset = Service.objects.all()
    #serializer_class = ServiceSerializer

#Check POST create search record
#Create Matches
#Return Match 
# class Searche(viewsets.ModelViewSet):
#     queryset = Searche.objects.all()
#     serializer_class = SearcheSerializer

# #Data Entry
# class Contractor(viewsets.ModelViewSet):
#     queryset = Contractor.objects.all()
#     serializer_class = ContractorSerializer

# class Client(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


    



