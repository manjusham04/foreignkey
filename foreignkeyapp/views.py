from django.shortcuts import render, get_object_or_404, redirect
from foreignkeyapp.models import Course, Student

# Add Course Page (default page)
def home(request):
    return render(request, 'home.html')


def course(request):
    courses = Course.objects.all()  # Fetch all courses from the database

    if request.method == "POST":
        # Check if this is an edit operation
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course_name")
        fee = request.POST.get("fee")

        if course_id:  # If course_id is provided, edit the existing course
            course = get_object_or_404(Course, id=course_id)
            course.course_name = course_name
            course.fee = fee
            course.save()
        else:  # Otherwise, add a new course
            Course.objects.create(course_name=course_name, fee=fee)

        return redirect("course")  # Refresh the page

    return render(request, "add_course.html", {"courses": courses})


# Add Student Page
def student(request):
    # Fetch all courses for the dropdown in the form
    courses = Course.objects.all()
    return render(request, 'add_student.html', {'course': courses})

# Add Course to Database
def add_coursedb(request):
    if request.method == "POST":
        # Get data from the form
        course_name = request.POST.get('course_name')  # Fetch the selected course from dropdown
        course_fee = request.POST.get('fee')

        # Save the new course to the database
        Course.objects.create(course_name=course_name, fee=course_fee)
        return redirect('student')  # Redirect to Add Student Page
    return render(request, 'add_course.html')  # Render Add Course Page for GET requests


# Add Student to Database
def add_studentdb(request):
    if request.method == "POST":
        # Get data from the form
        student_name = request.POST['student_name']
        student_address = request.POST['student_address']
        age = request.POST['age']
        joining_date = request.POST['date']
        course_id = request.POST['sel']

        # Fetch the selected course
        course = get_object_or_404(Course, id=course_id)

        # Save the new student to the database
        Student.objects.create(
            student_name=student_name,
            student_address=student_address,
            student_age=age,
            joining_date=joining_date,
            course=course
        )
        return redirect('show_details')  # Redirect to Show Details Page
    return redirect('course')  # Redirect back to Add Course Page for invalid requests

# Show All Student Details
def show_details(request):
    # Fetch all student records
    students = Student.objects.all()
    return render(request, 'show_details.html', {'students': students})

# Edit Student Details
def edit_student(request, student_id):
    # Fetch the student and all courses
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()

    if request.method == "POST":
        # Update student details from the form
        student.student_name = request.POST.get('student_name')
        student.student_address = request.POST.get('student_address')
        student.student_age = request.POST.get('student_age')
        student.joining_date = request.POST.get('joining_date')

        # Update the course
        course_id = request.POST.get('course')
        student.course = get_object_or_404(Course, id=course_id)

        # Save the updated student
        student.save()
        return redirect('show_details')  # Redirect to Show Details Page

    return render(request, 'edit_student.html', {'student': student, 'courses': courses})

# Delete Student
def delete_student(request, student_id):
    # Fetch the student by ID and delete
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('show_details')  # Redirect to Show Details Page
