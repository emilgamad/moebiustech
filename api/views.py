from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product, Question, Choice, Searche
from .serializers import ProductSerializer, QuestionSerializer, ChoiceSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response



class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class QuestionViewSet(ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['product']

class ChoiceViewSet(ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


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


    



