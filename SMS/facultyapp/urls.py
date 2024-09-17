from django.urls import path , include
from . import views

app_name = 'facultyapp'

urlpatterns = [
    path('', views.FacultyHomePage, name='FacultyHomePage'),

]