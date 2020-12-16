
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
        return render(request, "themes/dashboard.html", context)
    else:
        return render(request, "home/home.html")


def login(request):
    return redirect('accounts/log-in')

def register(request):
    return redirect('accounts/register')
