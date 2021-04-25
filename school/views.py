from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from school.models import School
from school.serializers import SchoolSerializer
# Create your views here.

class SchoolListView(APIView):

    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)


class SchoolView(APIView):

    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)
    
    

