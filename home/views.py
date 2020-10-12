
from django.shortcuts import render, redirect
from accounts.models import school_details
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from student.models import student_details
from settings.models import student_class

# Create your views here.
def home(request):
    try:
        required_school_data = school_details.objects.filter(
            username = request.session['username'],
            password = request.session['password']
        )

        if required_school_data:
            username = request.session['username']
            password = request.session['password']

            dictonary_to_pass ={
                'student_class':student_class.objects.filter(
                    username=required_school_data,
                ),
                'school_details': required_school_data[0],

            }
            return render(request, "boards/dashboard.html", dictonary_to_pass)
    except:
        return render(request,'home/home.html')
        


def max_nepali_day(request):
    from modules.getting_days import get_max_np_day
    year, month = request.GET['year'], request.GET['month']
    realMaxDate = {get_max_np_day(year, month)}
    print(realMaxDate)
    return HttpResponse(realMaxDate)