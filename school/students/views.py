from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm
from .predict_course import predict_course  # ✅ Import the ML model function

# View for Listing all students (with search)
def student_list(request):
    query = request.GET.get('search')
    if query:
        students = Student.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        ).order_by('-id')  # 👈 Order search results by newest first
    else:
        students = Student.objects.all().order_by('-id')  # 👈 Order all by newest first
    
    return render(request, 'students/student_list.html', {'students': students})

# View for creating a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)  # Save without committing yet
            # Predict the course
            student.course = predict_course(student.age, student.interest, student.gender)
            student.save()
            
            # Pass the predicted course to the success message
            return render(request, 'students/student_success.html', {
                'student': student,
                'message': f"The suited course for {student.first_name} is {student.course}."
            })
    else:
        form = StudentForm()
    
    return render(request, 'students/student_form.html', {'form': form})

# View for updating an existing student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)  # Save without committing yet
            # Predict the course again (in case age, gender, or interest changed)
            student.course = predict_course(student.age, student.interest, student.gender)
            student.save()

            # Pass the predicted course to the success message
            return render(request, 'students/student_success.html', {
                'student': student,
                'message': f"The course predicted for {student.first_name} is {student.course}."
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form})

# View for deleting a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})
