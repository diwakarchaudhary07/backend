from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['std_name', 'std_roll', 'std_image','std_email' ,'std_city']
