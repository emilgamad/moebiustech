from rest_framework import serializers

from app.models import Product, Question, Choice, Searche
from users.models import Contractor, Client


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "position",
            "service_slug",
            "service_label",
            "is_active",
        ]


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "label", "value"]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            #'product',
            "id",
            "position",
            "question_type",
            "question_label",
            "question_slug",
            "is_required",
            "is_multiple",
            "choices",
        ]


class SearcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searche
        fields = [
            "location_longitude",
            "location_langitude",
            "product_id",
            "answer",
            "phone_number",
            "contact_person",
            "address",
        ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "email",
            "number",
            "verified",
        ]


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = [
            "logo",
            "name",
            "zip_code",
            "product",
            "pub_date",
        ]
