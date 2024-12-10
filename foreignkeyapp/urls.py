from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course', views.course, name='course'),  # Default page (Add Course)
    path('student/', views.student, name='student'),  # Render Add Student page
    path('add_coursedb/', views.add_coursedb, name='add_coursedb'),  # Add Course to database
    path('add_studentdb/', views.add_studentdb, name='add_studentdb'),  # Add Student to database
    path('show_details/', views.show_details, name='show_details'),  # Show all Student details
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),  # Edit Student details
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),  # Delete Student
]
