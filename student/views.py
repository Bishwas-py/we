from django.shortcuts import render, redirect
from student.models import student_details
from settings.models import student_class
from accounts.models import school_details

# Create your views here.
def remove_student(request, ssname):
    username=request.session['username']
    password=request.session['password']
    student_data = student_details.objects.get(username=username, password=password, ssname=ssname)
    student_data.stpht.delete(save=True)
    student_data.delete()
    return redirect ('student')


def update_student(request, ssname):
    username = request.session['username']
    password=request.session['password']
    student_data = student_details.objects.get(
        username=username,
        password=password,
        ssname=ssname)

    try:
        cLass = student_class.objects.get(
            username=username, 
            password=password, 
            ssname=ssname)
    except:
        None
    
    student_address = request.POST.get(f'{student_data.ssname}1')
    student_class = request.POST.get(f'{student_data.ssname}2')
    student_fam_occupation = request.POST.get(f'{student_data.ssname}3')
    student_phone_num = request.POST.get(f'{student_data.ssname}4')
    stpht = request.FILES.get(f'{student_data.ssname}5')
    if stadd != None:
        student_data.stadd = stadd
        student_data.save()
    if student_classls != None:
        cLass.cList = student_classls
        student_data.save()
    if stfo != None:
        student_data.stfo = stfo
        student_data.save()
    if stpnum != None:
        student_data.stpnum = stpnum
        student_data.save()
    if stpht != None:
        student_data.stpht.delete(save=True)
        student_data.stpht = stpht
        student_data.save()
    return redirect('student')


def student(request):
    username=request.session['username']
    password=request.session['password']
    school_Details = school_details.objects.get(username=username, password=password)
    student_Class = student_class.objects.filter(connect_school=school_Details)
    student_Details = student_details.objects.filter(connect_school=school_Details)
    required_dict = {
        'school_details':school_Details,
        'student_class':student_Class,
        'student_details':student_Details
    }

    return render(request, 'themes/students.html', required_dict)



def add_student(request):
    username=request.session['username']
    password=request.session['password']
    if request.method == 'POST':
        school_details = school_details.objects.get(
            username=username,
            password=password
        )
        student_name = request.POST.get('stdname').rstrip()

        isStudentThere = (student_details.objects.filter(username=username, password=password, stname=stname))
        if isStudentThere:
            return render(request, 'themes/students.html', {'maxstd':f"{stname} is already created. Try something similar to: {stname} '1' or {stname} 'B'",'student_class':student_class.objects.filter(username=username, password=password),'school_details': school_details.objects.get(username=username, password=password), 'student_class': student_details.objects.filter(username=username, password=password)})

        student_short_name = stname.replace(' ','')
        student_address = request.POST.get('stdadd')
        student_class = student_class.objects.get(cList=request.POST.get('stdcls'))
        student_father = request.POST.get('stdfname')
        student_mother = request.POST.get('stdmname')
        student_fam_occupation = request.POST.get('stdfo')
        student_admission_date = request.POST.get('stdadate')
        student_phone_number= request.POST.get('stdpnum')
        student_date_of_birth = request.POST.get('stdbdate')
        student_photo = request.FILES.get('stdpht')
        student_data = student_details(
            student_short_name=student_short_name,
            school_details = school_details,
            student_class=student_class,
            username = username,
            password = password,
            student_name = student_name,
            student_address = student_address,
            student_father = student_father,
            student_mother = student_mother,
            student_fam_occupation = student_fam_occupation,
            student_admission_date = student_admission_date,
            student_phone_number = student_phone_number,
            student_date_of_birth = student_date_of_birth,
            student_photo = student_photo
        )
        student_data.save()
        return redirect('student')
    elif request.method == 'GET':
        from settings.models import student_class
        from accounts.models import school_details

        school_Details = school_details.objects.get(username=username, password=password)
        Classes = student_class.objects.filter(connect_school=school_Details)
        return render(request, 'themes/add_student.html', {'student_class':Classes, 'school_details':school_Details})
    # except:
    #     return redirect('home')