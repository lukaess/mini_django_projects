from django.db import models
from rest_framework import fields, serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'name', 'age'
        )