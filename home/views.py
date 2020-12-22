from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.models import School
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from student.models import Student
from school.models import Class


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        class_data = Class.objects.filter(connect_school=request.user)
        context = {'Class':class_data}
        return render(request, "contents/dashboard.html", context)
    else:
        return render(request, "home/home.html")


def login(request):
    return redirect('accounts/log-in')

def register(request):
    return redirect('accounts/register')
    dictonary_to_pass = {
        'Class': Class.objects.filter(
            connect_school=school_user,
        ),
        'School': school_user[0],

    }
    return render(request, "contents/dashboard.html", dictonary_to_pass)
    # except:
    #     return render(request,'home/home.html')


def max_nepali_day(request):
    from modules.getting_days import get_max_np_day
    year, month = request.GET['year'], request.GET['month']
    realMaxDate = {get_max_np_day(year, month)}
    print(realMaxDate)
    return HttpResponse(realMaxDate)


def todaydate(request):
    import nepali_datetime
    date = str(nepali_datetime.date.today()).split('-')
    date = {'year': date[0], 'month': date[1], 'day': date[2]}
    return JsonResponse(date)


def website(request):
    return render(request, 'index.html')

