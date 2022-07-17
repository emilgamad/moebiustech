from rest_framework import serializers

from app.models import Product, Question, Choice, Searche, Service
from users.models import Contractor, Client




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'position',
            'service_slug',
            'service_label',
            'is_active',
            ]

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'label',
            'value'
            ]

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = [
            #'product',
            'id',
            'position',
            'question_type',
            'question_label',
            'question_slug',
            'is_required',
            'is_multiple',
            'choices'
            ]



class ServiceSerializer(serializers.Serializer):
    product = ProductSerializer(many=True)
    question = QuestionSerializer(many=True)
    choices = ChoiceSerializer(many=True)
    

class SearcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searche
        fields = [
            'zip_code',
            'product',
            'question',
            'choice',
            'first_name',
            'last_name',
            'email',
            'number',
            'project_location'
            ]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'email',
            'number',
            'verified',
            ]

class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = [
            'logo',
            'name',
            'zip_code',
            'product',
            'pub_date',
            ]

