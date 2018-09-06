from django.urls import path

from . import views

schoolList = views.SchoolView.as_view({
    'get': 'list',
    'post': 'create'})
studentList = views.StudentView.as_view({
    'get': 'list',
    'post': 'create'})
schoolDetail = views.SchoolView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'})
studentDetail = views.StudentView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'})


urlpatterns = [
    path('schools/', schoolList),
    path('students/', studentList),
    path('schools/<int:pk>/', schoolDetail),
    path('students/<int:pk>/', studentDetail),
]
