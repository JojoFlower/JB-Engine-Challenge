import uuid
from django.db import models


class School(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='School Name'
    )
    max_students = models.PositiveIntegerField(
        verbose_name='Maximum Number of Students'
    )


class Student(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Last Name'
    )
    student_id = models.CharField(
        max_length=20,
        verbose_name='Student ID'
    )
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        verbose_name='Student School'
    )
    identification_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
