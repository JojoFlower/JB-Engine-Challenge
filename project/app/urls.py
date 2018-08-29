from django.conf.urls import url

from . import views

urlpatterns = [
    url('schools/', views.SchoolList.as_view()),
    url('students/', views.StudentList.as_view()),
]
