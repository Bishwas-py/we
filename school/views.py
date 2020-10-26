from django.shortcuts import render, HttpResponse
from accounts.models import School 
from school.models import Class
# Create your views here.
def profile(request):
    username= request.session['username']
    password=request.session['password']
    return render(request, "settings/profile.html", {'stc':stdClass.objects.filter(username=username, password=password), 'sdata': schoolDetails.objects.get(username=username, password=password)})


def addclass(request):
    username = request.session['username']
    password = request.session['password']
    
    get_class = request.POST.get('class')
    class_list = ["Grade "+ str(i) for i in range(1, 13)]+["Class "+ str(i) for i in range(1, 13)]+[str(i) for i in range(1, 13)]+['Montessori','Nursery','L.K.G','U.K.G','Kindergarten','Kinder Garten','K.G']
    
    school_data = School.objects.get(username=username, password=password)
    if get_class in class_list:
        if not Class.objects.filter(connect_school=school_data, class_list=get_class):
            
            class_data = Class(connect_school=school_data, class_list=get_class)
            class_data.save()
            return HttpResponse(get_class)
        else:
            return HttpResponse(2) # 2 means already created
    else:
        return HttpResponse(0) # 0 means false i.e NONSENSE

def automatic_class(request):
    create_class = ['Nursery','L.K.G','U.K.G','Kindergarten']+["Class "+ str(i) for i in range(1, 11)]
    username = request.session['username']
    password = request.session['password']
    already_created = []
    if request.method == 'POST':
        school_data = School.objects.get(username=username, password=password)
        for class_ in create_class:
            if not Class.objects.filter(connect_school=school_data,class_list=class_):
                class_data = Class(connect_school=school_data, class_list=class_)
                class_data.save()
            else:
                already_created.append(class_)
        if len(already_created) == len(create_class):
            return HttpResponse(0)
        else:
            return HttpResponse(1)
    else:
        return HttpResponse(0)
        