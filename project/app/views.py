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


class StudentNestedView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['schools_pk'])

    def create(self, request, schools_pk):
        schoolMaxStudents = School.objects.get(pk=schools_pk).max_students
        schoolStudentsNumber = len(School.objects.get(pk=schools_pk).student_set.all())

        if schoolStudentsNumber < schoolMaxStudents:
            student = Student(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                student_id=request.data['student_id'],
                school=School.objects.get(pk=schools_pk))
            student.save()
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            return Response({'Error': 'Too much students'}, status=status.HTTP_403_FORBIDDEN)
