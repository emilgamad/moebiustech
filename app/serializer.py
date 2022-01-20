from rest_framework import serializers

from .models import Question, Product, Choice


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'create_date',
            'contractors'
        ]

    