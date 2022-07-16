from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product, Question, Choice, Searche, QuestionChoices
from users.models import Contractor, Client
from .serializers import ProductSerializer, QuestionSerializer, ChoiceSerializer, \
    SearcheSerializer, ClientSerializer, ContractorSerializer, QuestionChoicesSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response


class Product(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Question(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['product']

class Choice(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filterset_fields = ['question']

class QuestionChoices(viewsets.ModelViewSet):
    queryset = QuestionChoices.objects.all()
    serializer_class = QuestionChoicesSerializer


#Check POST create search record
#Create Matches
#Return Match 
class Searche(viewsets.ModelViewSet):
    queryset = Searche.objects.all()
    serializer_class = SearcheSerializer

#Data Entry
class Contractor(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class Client(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    



