from rest_framework import viewsets
from rest_framework.response import Response
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer


class SchoolList(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
