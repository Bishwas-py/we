from django.shortcuts import render, redirect
from school.models import Class
from accounts.models import School
from student.models import Student

# Create your views here.


def settings(request):
    username = request.session['username']
    password = request.session['password']
    school_data = School.objects.get(
        username=username, password=password)
    required_dictionary = {
        'Class': Class.objects.filter(
            connect_school=school_data,
        ),

        'School': school_data,

        'Student': Student.objects.filter(
            connect_school=school_data
        )
    }
    return render(request, "themes/settings.html", required_dictionary)

