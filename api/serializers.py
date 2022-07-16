from rest_framework import serializers

from app.models import Product, Question, Choice, Searche, QuestionChoices
from users.models import Contractor, Client


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'is_active',
            'position',
            ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'product',
            'question_text',
            'position',
            'is_active'
            ]

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'is_active',
            'position',
            'question',
            'choice_text'
            ]

class QuestionChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoices
        fields = [
            'id',
            'value',
            'label',
            ]

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

