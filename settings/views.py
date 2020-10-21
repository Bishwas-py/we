from django.shortcuts import render, redirect
from school.models import student_class
from accounts.models import school_details
from student.models import student_details

# Create your views here.


def settings(request):
    username = request.session['username']
    password = request.session['password']
    school_data = school_details.objects.get(
        username=username, password=password)
    required_dictionary = {
        'student_class': student_class.objects.filter(
            connect_school=school_data,
        ),

        'school_details': school_data,

        'student_details': student_details.objects.filter(
            connect_school=school_data
        )
    }
    return render(request, "themes/settings.html", required_dictionary)

