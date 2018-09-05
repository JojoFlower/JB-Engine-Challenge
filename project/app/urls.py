from django.conf.urls import url

from . import views

schoolView = views.SchoolView.as_view({
    'get': 'list',
    'post': 'create'})
studentView = views.StudentView.as_view({
    'get': 'list',
    'post': 'create'})


urlpatterns = [
    url('schools/', schoolView),
    url('students/', studentView),
]
