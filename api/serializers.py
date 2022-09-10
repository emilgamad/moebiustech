from rest_framework import serializers

from app.models import Product, Question, Choice, Searche, Result, Contractor


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
            "product",
            "answer",
            "phone_number",
            "contact_person",
            "address",
            "result",
        ]


class ContractorSerializer(serializers.ModelSerializer):
    experties = ChoiceSerializer(many=True)

    class Meta:
        model = Contractor
        fields = [
            "id",
            "company_name",
            "company_person",
            "field",
            "phone_number",
            "address",
            "email",
            "about",
            "experties",
        ]


class ResultSerializer(serializers.ModelSerializer):
    # searche = serializers.SerializerMetodField('')
    # nearby_contractors = ContractorSerializer(many=True)
    # oor_contractors = ContractorSerializer(many=True)
    class Meta:
        model = Result
        fields = ["id", "nearby_contractors", "oor_contractors"]
