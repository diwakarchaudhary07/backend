from django.contrib import admin
from django.urls import path  
from .views import student_info, add_student, edit_student, delete_student


urlpatterns = [
    path('students', student_info, name='student_info'),
    path('add/', add_student, name='add_student'),
    path('edit/<int:id>/', edit_student, name='edit_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
]