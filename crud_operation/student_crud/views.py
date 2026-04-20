from django.shortcuts import render
from .models import Student


# Create your views here.
def student_info(request):
    students = Student.objects.all()
    return render(request, 'other.html', {'students': students})
