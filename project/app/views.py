from rest_framework import viewsets
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
