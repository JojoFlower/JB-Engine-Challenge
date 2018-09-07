from rest_framework import viewsets
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):
        schoolId = int(request.data['school'])
        schoolMaxStudents = School.objects.get(pk=schoolId).max_students
        schoolStudentsNumber = len(School.objects.get(pk=schoolId).student_set.all())

        if schoolStudentsNumber < schoolMaxStudents:
            return super().create(request)
        else:
            return Response({'Error': 'Too much students'}, status=status.HTTP_403_FORBIDDEN)


class SchoolNestedView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentNestedView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['schools_pk'])
