from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import StudentSerializer
from drfapp.models import Student


class TestView(APIView):

    permission_classes = (IsAuthenticated, )


    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        #specifying many = true to get the list of all Students from the database
        serializers = StudentSerializer(queryset, many = True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)