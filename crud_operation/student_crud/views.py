from django.shortcuts import render, redirect ,get_object_or_404
from .models import Student
from .forms import StudentForm


# Create your views here.
def student_info(request):
    students = Student.objects.all()
    return render(request, 'other.html', {'students': students})


# Create
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# Read
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Update
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

# Delete
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
