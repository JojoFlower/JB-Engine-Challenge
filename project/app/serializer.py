from .models import School, Student
from rest_framework import serializers


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


class SchoolSerializer(serializers.ModelSerializer):
    student_set = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='identification_id')

    class Meta:
        model = School
        fields = (
            'name',
            'max_students',
            'student_set'
        )
