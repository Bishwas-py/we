from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from student.models import Student
from school.models import Class
from accounts.models import School

# Create your views here.
def remove_student(request, ssname):
    username=request.session['username']
    password=request.session['password']
    student_data = Student.objects.get(username=username, password=password, ssname=ssname)
    student_data.stpht.delete(save=True)
    student_data.delete()
    return redirect ('student')


def update_student(request, ssname):
    username = request.session['username']
    password=request.session['password']
    student_data = Student.objects.get(
        username=username,
        password=password,
        ssname=ssname)

    try:
        cLass = Class.objects.get(
            username=username, 
            password=password, 
            ssname=ssname)
    except:
        None
    
    student_address = request.POST.get(f'{student_data.ssname}1')
    Class = request.POST.get(f'{student_data.ssname}2')
    student_fam_occupation = request.POST.get(f'{student_data.ssname}3')
    student_phone_num = request.POST.get(f'{student_data.ssname}4')
    stpht = request.FILES.get(f'{student_data.ssname}5')
    if stadd != None:
        student_data.stadd = stadd
        student_data.save()
    if Classls != None:
        cLass.cList = Classls
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
    school_data = School.objects.get(username=username, password=password)
    Classes = Class.objects.filter(connect_school=school_data)
    student_data = Student.objects.filter(connect_school=school_data)
    required_dict = {
        'School':school_data,
        'Class':Classes,
        'Student':student_data
    }

    return render(request, 'themes/students.html', required_dict)

def student_profile(request, ssname):
    username=request.session['username']
    password=request.session['password']
    school_data = School.objects.get(username=username, password=password)
    Class_data = Class.objects.filter(connect_school=school_data)
    student_data = Student.objects.filter(connect_school=school_data, short_name=ssname)
    required_dict = {
        'School':school_data,
        'Class':Class_data,
        'Student':student_data
    }

    return render(request, 'themes/more_info_student.html', required_dict)

def add_student(request):
    username=request.session['username']
    password=request.session['password']

    from student.models import Student
    from school.models import Class
    from accounts.models import School

    if request.method == 'POST':
        school_data = School.objects.get(
                    username=username,
                    password=password
        )
        class_ = request.POST.get('class')
        name = request.POST.get('name').rstrip()
        gender = request.POST.get('gender')
        ethnicity=request.POST.get('ethnicity')
        print('name', name)
        try:
            class_list=Class.objects.get(connect_school=school_data, class_list=class_)
        except:
            required_dict = {
                'success_value':'danger',
                'success_message':f"The class{'es' if class_ == '' else ''} {'[' if class_ != '' else ''}{class_}{']' if class_ != '' else ''} {'are' if class_ == '' else 'is'} not created yet",
                'success_body':f"Please create class{'es' if class_ == '' else ''} {'[' if class_ != '' else ''} {class_} {']' if class_ != '' else ''} in the upper 'Class' option, fill the form correctly and submit again.",
                'success_remarks':'Faliure'
            }
            return JsonResponse(required_dict)
        short_name = name.replace(' ','')
        address = request.POST.get('address')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        fam_occupation = request.POST.get('fam_occupation')
        """   Admission DATES    """
        from modules.date_works import convert
        admission_year, admission_month, admission_day = request.POST.get('admission_year'), request.POST.get('admission_month'), request.POST.get('admission_day')
        print('admission_year:',admission_year, 'Month: ', admission_month, 'Day:', admission_day)
        admission_dates = convert(admission_year, admission_month, admission_day)
        nepali_admission_date = admission_dates['np']
        eng_admission_date = admission_dates['en']
        """   DATE OF BIRTH DATES    """
        dob_year, dob_month, dob_day = request.POST['dob_year'], request.POST['dob_month'], request.POST['dob_day']
        dob_dates = convert(dob_year, dob_month, dob_day)
        nepali_dob_date =  dob_dates['np']
        eng_dob_date = dob_dates['en']

        phone_number= request.POST.get('phone_number')
        photo = request.FILES.get('photo')
        print('photo:',photo)

        
        is_student_created = Student.objects.filter(
                connect_school=school_data,
                name=name,
                Class=class_list,
                mother=mother,
                father=father,
                eng_dob_date=eng_dob_date
            )

        if is_student_created:
            required_dict = {
                'success_value':'danger',
                'success_message':f"{name} is already created",
                'success_body':f"{name} is already created. Try something similar to: {name} '1' or {name} 'B'",
                'success_remarks':'Faliure'
                }
            return JsonResponse(required_dict)

        student_data = Student(
            connect_school=school_data,
            name = name,
            gender=gender,
            ethnicity=ethnicity,
            short_name=short_name,
            Class=class_list,
            address = address,
            father = father,
            mother = mother,
            fam_occupation = fam_occupation,
            # DATES - ADmission
            nepali_admission_date = nepali_admission_date,
            eng_admission_date = eng_admission_date,
            # DATES - DATE OF BIRTH
            nepali_dob_date = nepali_dob_date,
            eng_dob_date = eng_dob_date,
            
            phone_number = phone_number,
            photo = photo
        )
        student_data.save()
        required_dict = {
            'success_value':'success',
            'success_message':f'{name} is created.',
            'success_body':f'The student you submitted in created now. You can add more students.',
            'success_remarks':'Successful'
            }
        return JsonResponse(required_dict)
    elif request.method == 'GET':
        from school.models import Class
        from student.models import Student
        from accounts.models import School

        school_data = School.objects.get(username=username, password=password)
        gender = Student.gender_choices
        ethnicity = Student.ethnic_groups
        Classes = Class.objects.filter(connect_school=school_data)
        return render(request, 'themes/add_student.html', {
            'Class':Classes,
            'School':school_data,
            'gender':gender,
            'ethnicity':ethnicity
            })
    # except:
    #     return redirect('home')