from django.shortcuts import render
from settings.models import student_class
from school.models import schoolDetails

# Create your views here.
def settings(request):
    username = request.session['username']
    password = request.session['password']
    classes = request.POST.get('classes')
    if classes != None:
        class_data = student_class(cList=classes, username=username, password=password)
        class_data.save()
    required_dictionary = {
        'student_classes':student_class.objects.filter(
            username=username,
            password=password
        ),

        'sdata':schoolDetails.objects.filter(
            username=username,
            password=password
        )[0],

        'std': stdDetails.objects.filter(
            username=request.session['username'],
            password=request.session['password']
        )
        }
    return render(request, "settings.html", )