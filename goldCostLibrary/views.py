# views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student  # Import the Student model

def home(request):
    return render(request, 'index.html')

def students(request):
    students_list = Student.objects.all()  # Fetch all students to display
    return render(request, 'students.html', {'students': students_list})

def addNew(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('contact_number')
        email = request.POST.get('email_id')
        seat = request.POST.get('seat_number')
        date = request.POST.get('joining_date')
        fee = request.POST.get('monthly_fee')

        # Use a default image URL for student profiles
        default_image_url = "https://media.istockphoto.com/id/1334218189/photo/girl-doing-homework-or-online-education.jpg?s=1024x1024&w=is&k=20&c=OxPMmTj06BqYZcZ3k_3PtNIfTtyb0-v3_s49y9TZKIc="
        
        # Create a new student instance
        student = Student(
            name=name,
            contact_number=number,
            email_id=email,
            seat_number=seat,
            joining_date=date,
            monthly_fee=fee,
            profile_image=default_image_url  # Set the default image URL
        )
        student.save()  # Save the student to the database

        # Add a success message
        messages.success(request, f"Student '{name}' has been successfully added.")
        

    return render(request, 'addNew.html')
