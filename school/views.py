from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, JsonResponse
from accounts.models import School 
from school.models import Class, Subject
from student.models import Student
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
            required_dict = {
                'success_value':'primary',
                'success_message':f"Classes are already created.",
                'success_body':f"The class are already created. You can procced to next step.",
                'success_remarks':'Success'
                }
            return JsonResponse(required_dict)
        else:
            required_dict = {
                'success_value':'success',
                'success_message':f"Classes created automatically",
                'success_body':f"The class are already created automatically. You can procced to next step.",
                'success_remarks':'Success'
                }
            return JsonResponse(required_dict)
    else:
        return HttpResponse(0)
        
def add_subject(request):
    if request.method == 'GET':
        return redirect('settings')
    elif request.method == 'POST':
        print(request.POST)
        username = request.session['username']
        password = request.session['password']
        class_ = request.POST.get('class')
        subject = request.POST.get('subject')
        school_data = School.objects.get(username=username, password=password)
        connect_class = Class.objects.get(class_list=class_)
        subject_required = Subject(
            connect_class=connect_class,
            subjects = subject
        )
        subject_required.save()

        required_data = {
            'success_value':'success',
            'success_message': f'{subject} created successfully.',
            'success_body': f"The {subject} subject created. You can procced to next step.",
            'success_remarks': f'Success'
        }
        return JsonResponse(required_data)
