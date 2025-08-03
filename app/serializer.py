
"""
Serializers for the app module.
"""

from rest_framework import serializers

from .models import Question, Product, Choice


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    class Meta:
        model = Product
        fields = ["name", "create_date", "contractors"]
