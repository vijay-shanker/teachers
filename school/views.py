from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import GenericAPIView 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from school.models import School
from school.serializers import SchoolSerializer
from drf_yasg.utils import swagger_auto_schema


class SchoolListView(APIView):
    @swagger_auto_schema(tags=['School'])
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)


class SchoolView(GenericAPIView):
    serializer_class = SchoolSerializer

    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    @swagger_auto_schema(tags=['School'])
    def get(self, request, pk):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)
    
    @swagger_auto_schema(tags=['School'])
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            school = serializer.save()
            return Response(school.data, status=status.HTTP_201_created)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
