from django.contrib import admin
from django.urls import path  
from .views import student_info


urlpatterns = [
    path('students/', student_info, name='student_info'),
]