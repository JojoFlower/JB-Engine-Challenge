from .models import School, Student
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'name',
            'max_students'
        )


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'student_id',
            'school',
            'identification_id'
        )
