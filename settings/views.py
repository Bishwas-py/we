from django.shortcuts import render, redirect
from school.models import Class
from accounts.models import School
from student.models import Student

# Create your views here.


def settings(request):

    required_dictionary = {
        'Class': Class.objects.filter(
            connect_school=request.user,
        ),
        'Student': Student.objects.filter(
            connect_school=request.user
        )
    }
    return render(request, "contents/settings.html", required_dictionary)

