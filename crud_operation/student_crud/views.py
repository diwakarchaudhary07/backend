from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# ✅ READ (List)
def student_info(request):
    students = Student.objects.all()
    return render(request, 'other.html', {'students': students})


# ✅ CREATE
# def add_student(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST, request.FILES)  # 🔥 important
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm()

#     return render(request, 'student_form.html', {'form': form})


# # ✅ UPDATE
# def edit_student(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == "POST":
#         form = StudentForm(request.POST, request.FILES, instance=student)  # 🔥 important
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm(instance=student)

#     return render(request, 'student_form.html', {'form': form})


# # ✅ DELETE
# def delete_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return redirect('student_list')