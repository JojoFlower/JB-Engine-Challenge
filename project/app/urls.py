from django.urls import include, path
from rest_framework_nested import routers

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

schoolRouter = routers.SimpleRouter()
schoolRouter.register(r'schools', views.SchoolNestedView)
studentRouter = routers.NestedSimpleRouter(schoolRouter, r'schools', lookup='schools')
studentRouter.register(r'students', views.StudentNestedView)

urlpatterns = [
    path('schools/', schoolList),
    path('students/', studentList),
    path('schools/<int:pk>/', schoolDetail),
    path('students/<int:pk>/', studentDetail),
    path('', include(studentRouter.urls)),
]
