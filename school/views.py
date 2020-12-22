from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, JsonResponse
from accounts.models import School 
from school.models import Class, Subject, SubjectsList
from student.models import Student
# Create your views here.


def add_class(request):
    get_class = request.POST.get('class')
    class_name = ["Grade " + str(i) for i in range(1, 13)] +\
                 ["Class " + str(i) for i in range(1, 13)] +\
                 [str(i) for i in range(1, 13)] +\
                 ['Montessori', 'Nursery', 'L.K.G', 'U.K.G', 'Kindergarten', 'Kinder Garten', 'K.G']

    if get_class in class_name:
        if not Class.objects.filter(connect_school=request.user, class_name=get_class):
            class_data = Class(connect_school=request.user, class_name=get_class)
            class_data.save()
            return HttpResponse(get_class)
        else:
            return HttpResponse(2) # 2 means already created
    else:
        return HttpResponse(0) # 0 means false i.e NONSENSE


def add_subject(request):
    if request.method == 'POST':
        get_class = request.POST.get('class')
        get_subjects = request.POST.get('subject').split(',')

        class_data = Class.objects.get(class_name=get_class, connect_school=request.user)

        subjects_array = list()
        for sub in get_subjects:
            try:
                is_sub = SubjectsList.objects.get(sub=sub)         # if SubjectList has the given 'subject' in it.
            except:
                is_sub = SubjectsList.objects.create(sub=sub)      # if SubjectList don't have given 'subject' in it.
            subjects_array.append(is_sub)

        class_data = Class.objects.get(
            class_name=get_class,
            connect_school=request.user
        )

        if subjects_array:
            try:
                subject_required = Subject.objects.get(
                    connect_class=class_data
                )
            except:
                subject_required = Subject(
                    connect_class=class_data
                )
            subject_required.save()
            subject_required.subject.add(*subjects_array)
            subject_required.save()

        required_data = {
            'success_value':'success',
            'success_message': f'{get_subjects} created successfully.',
            'success_body': f"The {get_subjects} subject created. You can procced to next step.",
            'success_remarks': f'Success'
        }
        return JsonResponse(required_data)
    elif request.method == 'GET':
        return redirect('settings')
