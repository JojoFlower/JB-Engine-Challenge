from rest_framework.views import APIView
from rest_framework.response import Response
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer


class SchoolList(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)


class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
