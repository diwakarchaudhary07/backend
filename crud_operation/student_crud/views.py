from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# ✅ READ (List)
def student_info(request):
    students = Student.objects.all()
    return render(request, 'other.html', {'students': students})



def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            std_name=request.POST['name'],
            std_roll=request.POST['roll'],
            std_image=request.FILES['image'],
            std_email=request.POST['email'],
            std_city=request.POST['city']
        )
        return redirect('student_info')
    return render(request, 'add.html')

def delete_student(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('student_info')


# # Update Data
def edit_student(request, id):
    data = Student.objects.get(id=id)


    if request.method == 'POST':
        data.std_name = request.POST['name']
        data.std_roll = request.POST['roll']
        data.std_email = request.POST['email']
        data.std_city = request.POST['city']


        if request.FILES.get('image'):
            data.std_image = request.FILES['image']


        data.save()
        return redirect('student_info')


    return render(request, 'edit.html', {'data': data})
