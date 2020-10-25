from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from student.models import student_details
from school.models import student_class
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
    student_data = student_details.objects.filter(connect_school=school_Details)
    required_dict = {
        'school_details':school_Details,
        'student_class':student_Class,
        'student_details':student_data
    }

    return render(request, 'themes/students.html', required_dict)



def add_student(request):
    username=request.session['username']
    password=request.session['password']

    from student.models import student_details
    from school.models import student_class
    from accounts.models import school_details

    if request.method == 'POST':
        school_details = school_details.objects.get(
                    username=username,
                    password=password
        )
        Class = request.POST.get('student_class')
        print('Class:  ', Class)
        student_name = request.POST.get('student_name').rstrip()
        gender = request.POST.get('gender')
        ethnicity=request.POST.get('ethnicity')
        print('student_name', student_name)
        try:
            class_list=student_class.objects.get(class_list=Class)
        except:
            required_dict = {
                'success_value':'danger',
                'success_message':f"Classes aren't created yet",
                'success_body':f"Please create classes in the upper 'Class' option, fill the form correctly and submit again.",
                'success_remarks':'Faliure'
            }
            return JsonResponse(required_dict)
        student_short_name = student_name.replace(' ','')
        student_address = request.POST.get('student_address')
        student_father = request.POST.get('student_father')
        student_mother = request.POST.get('student_mother')
        student_fam_occupation = request.POST.get('student_fam_occupation')
        """   Admission DATES    """
        from modules.date_works import convert
        admission_year, admission_month, admission_day = request.POST.get('admission_year'), request.POST.get('admission_month'), request.POST.get('admission_day')
        print('admission_year:',admission_year, 'Month: ', admission_month, 'Day:', admission_day)
        admission_dates = convert(admission_year, admission_month, admission_day)
        student_nepali_admission_date = admission_dates['np']
        student_eng_admission_date = admission_dates['en']
        """   DATE OF BIRTH DATES    """
        dob_year, dob_month, dob_day = request.POST['dob_year'], request.POST['dob_month'], request.POST['dob_day']
        dob_dates = convert(dob_year, dob_month, dob_day)
        student_nepali_dob_date =  dob_dates['np']
        student_eng_dob_date = dob_dates['en']

        student_phone_number= request.POST.get('student_phone_number')
        student_photo = request.FILES.get('student_photo')
        print('student_photo:',student_photo)
        student_class = student_class.objects.get(class_list=class_list)
        
        is_student_created = student_details.objects.filter(
                connect_school=school_details,
                student_name=student_name,
                student_class=student_class,
                student_mother=student_mother,
                student_father=student_father,
                student_eng_dob_date=student_eng_dob_date
            )

        if is_student_created:
            required_dict = {
                'success_value':'danger',
                'success_message':f"{student_name} is already created",
                'success_body':f"{student_name} is already created. Try something similar to: {student_name} '1' or {student_name} 'B'",
                'success_remarks':'Faliure'
                }
            return JsonResponse(required_dict)

        
        student_data = student_details(
            connect_school=school_details,
            student_name = student_name,
            gender=gender,
            ethnicity=ethnicity,
            student_short_name=student_short_name,
            student_class=student_class,
            student_address = student_address,
            student_father = student_father,
            student_mother = student_mother,
            student_fam_occupation = student_fam_occupation,
            # DATES - ADmission
            student_nepali_admission_date = student_nepali_admission_date,
            student_eng_admission_date = student_eng_admission_date,
            # DATES - DATE OF BIRTH
            student_nepali_dob_date = student_nepali_dob_date,
            student_eng_dob_date = student_eng_dob_date,
            
            student_phone_number = student_phone_number,
            student_photo = student_photo
        )
        student_data.save()
        required_dict = {
            'success_value':'success',
            'success_message':f'{student_name} is created.',
            'success_body':f'The student you submitted in created now. You can add more students.',
            'success_remarks':'Successful'
            }
        return JsonResponse(required_dict)
    elif request.method == 'GET':
        from school.models import student_class
        from student.models import student_details
        from accounts.models import school_details

        school_details = school_details.objects.get(username=username, password=password)
        student_details = student_details.objects.first()
        gender = student_details._meta.get_field('gender').choices
        ethnicity = student_details._meta.get_field('ethnicity').choices
        Classes = student_class.objects.filter(connect_school=school_details)
        return render(request, 'themes/add_student.html', {
            'student_class':Classes,
            'school_details':school_details,
            'gender':gender,
            'ethnicity':ethnicity
            })
    # except:
    #     return redirect('home')