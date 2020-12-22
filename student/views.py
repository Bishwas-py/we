from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from student.models import Student
from school.models import Class, Subject, MarksReport, SubjectsList
from accounts.models import School


def student_table(request):
    class_data = Class.objects.filter(connect_school=request.user)
    student_data = Student.objects.filter(connect_school=request.user)
    required_dict = {
        'Class': class_data,
        'Student': student_data
    }
    return render(request, 'contents/students_table.html', required_dict)


def student_report(request):
    if request.method == 'GET':
        class_data = Class.objects.filter(connect_school=request.user)
        context = {
            'Class':class_data,
        }
        return render(request, 'contents/student_report.html', context)


def student_report_class_wise(request, class_):
    class_data = Class.objects.get(connect_school=request.user, class_name=class_)
    subject_data = Subject.objects.filter(connect_class=class_data)
    student_data = Student.objects.filter(connect_school=request.user, Class=class_data)
    try:
        marks_report_data = MarksReport.objects.get(subject=subject_data[0])
    except MarksReport.DoesNotExist:
        marks_report_data = False

    if request.method == 'GET':
        context = {
            'MarksReport': marks_report_data,
            'Class': class_data,
            'Student': student_data,
            'Subject': subject_data,
        }
        return render(request, 'contents/student_report_class_wise.html', context)
    elif request.method == "POST":
        get_student = request.POST.get('student')
        student_data = Student.objects.get(
            connect_school=request.user,
            name=get_student,
        )
        """ Creation of Full Marks and Pass Marks for each subjects for the first time. """
        for subject in student_data:
            for sub in subject.subject.all:
                get_subject = request.POST.get(f'{sub}')
                marks_report_create = MarksReport.objects.filter(
                    school=request.user,
                    subject=SubjectsList.objects.get(sub=sub),
                )
                if marks_report_create:
                    pass
                else:
                    marks_report_create = MarksReport(
                        school=request.user,
                        student=subject_data,
                        subject=SubjectsList.objects.get(sub=sub),
                        full_marks=request.POST.get(f'{sub}_fm'),
                        pass_marks=request.POST.get(f'{sub}_pm')
                    )
                marks_report_create.save()


def student_profile(request, short_name):
    class_data = Class.objects.filter(connect_school=request.user)
    student_data = Student.objects.filter(connect_school=request.user, short_name=short_name)
    required_dict = {
        'School': request.user,
        'Class': class_data,
        'Student': student_data
    }
    return render(request, 'contents/more_info_student.html', required_dict)


def add_student(request):
    if request.method == 'POST':
        get_class = request.POST.get('class')
        name = request.POST.get('name').rstrip()
        gender = request.POST.get('gender')
        ethnicity = request.POST.get('ethnicity')
        try:
            class_name = Class.objects.get(connect_school=request.user, class_name=get_class)
        except:
            required_dict = {
                'success_value': 'danger',
                'success_message': f"The class{'es' if get_class == '' else ''} {'[' if get_class != '' else ''}{get_class}{']' if get_class != '' else ''} {'are' if get_class == '' else 'is'} not created yet",
                'success_body': f"Please create class{'es' if get_class == '' else ''} {'[' if get_class != '' else ''} {get_class} {']' if get_class != '' else ''} in the upper 'Class' option, fill the form correctly and submit again.",
                'success_remarks': 'Failure'
            }
            return JsonResponse(required_dict)

        short_name = name.replace(' ', '')
        address = request.POST.get('address')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        fam_occupation = request.POST.get('fam_occupation')
        """   Admission DATES    """
        from modules.date_works import convert
        admission_year, admission_month, admission_day = request.POST.get('admission_year'),\
                                                         request.POST.get('admission_month'),\
                                                         request.POST.get('admission_day')
        print('admission_year:', admission_year, 'Month: ', admission_month, 'Day:', admission_day)
        admission_dates = convert(admission_year, admission_month, admission_day)
        nepali_admission_date = admission_dates['np']
        eng_admission_date = admission_dates['en']
        admission_date = admission_dates['nm']
        """   DATE OF BIRTH DATES    """
        dob_year, dob_month, dob_day = request.POST['dob_year'], request.POST['dob_month'], request.POST['dob_day']
        dob_dates = convert(dob_year, dob_month, dob_day)
        nepali_dob_date = dob_dates['np']
        eng_dob_date = dob_dates['en']
        dob_date = dob_dates['nm']

        phone_number = request.POST.get('phone_number')
        photo = request.FILES.get('photo')
        subject = Subject.objects.filter(connect_class=class_name)
        if not subject:
            required_dict = {
                'success_value': 'danger',
                'success_message': f"Please create some subjects.",
                'success_body': f"""Please create some subjects like: English, Nepali, etc. <a href="/school/""" +
                """create-subjects" target="_blank">Click here</a> to create subjects. Visit there, create""" +
                """ subjects and come back here.""",
                'success_remarks': 'Failure'
                }
            return JsonResponse(required_dict)
        print('subject::: ', subject)
        is_student_created = Student.objects.filter(
                connect_school=request.user,
                name=name,
                Class=class_name,
                mother=mother,
                father=father,
                eng_dob_date=eng_dob_date
            )
        if is_student_created:
            required_dict = {
                'success_value': 'danger',
                'success_message': f"{name} is already created",
                'success_body': f"{name} is already created. Try something similar to: {name} '1' or {name} 'B'",
                'success_remarks': 'Failure'
                }
            return JsonResponse(required_dict)

        student_data = Student(
            connect_school=request.user,
            name=name,
            gender=gender,
            ethnicity=ethnicity,
            short_name=short_name,
            Class=class_name,
            address=address,
            father=father,
            mother=mother,
            fam_occupation=fam_occupation,
            # DATES - ADmission
            nepali_admission_date=nepali_admission_date,
            eng_admission_date=eng_admission_date,
            admission_date=admission_date,

            # DATES - DATE OF BIRTH
            nepali_dob_date=nepali_dob_date,
            eng_dob_date=eng_dob_date,
            dob_date=dob_date,
            
            phone_number=phone_number,
            photo=photo,

        )
        student_data.save()
        student_data.subject.add(*subject)
        # student_data.save()
        required_dict = {
            'success_value': 'success',
            'success_message': f'{name} is created.',
            'success_body': f'The student you submitted in created now. You can add more students.',
            'success_remarks':' Successful'
            }
        return JsonResponse(required_dict)
    elif request.method == 'GET':
        gender = Student.gender_choices
        ethnicity = Student.ethnic_groups
        class_data = Class.objects.filter(connect_school=request.user)
        return render(request, 'contents/add_student.html', {
            'Class': class_data,
            'gender': gender,
            'ethnicity': ethnicity
            })


def delete(request, short_name):
    print('short_name', short_name)
    if request.method == 'POST':
        username=request.session['username']
        password=request.POST.get('password')

        try:
            print('Success')
            school_data = School.objects.get(username=username, password=password)
            student_data = Student.objects.get(connect_school=school_data, short_name=short_name)
            print('Success')
            student_data.photo.delete(save=True)
            student_data.delete()
            required_dict = {
                    'success_value':'success',
                    'success_message':f"The student is deleted successfullly.",
                    'success_body':f"You will be redirected to 'Our student' table page.",
                    'success_remarks':'Success'
            }
            return JsonResponse (required_dict)
        except:
            print('Failed')
            required_dict = {
                'success_value':'danger',
                'success_message':f"The student isn't deleted.",
                'success_body':f"Please re-type your actual password and try again.",
                'success_remarks':'Faluire'
            }
            return JsonResponse (required_dict)
    else:
        return redirect('student')


def update_student(request, short_name):
    student_data = Student.objects.get(
        connect_school=request.user,
        short_name=short_name
    )

    return redirect('student')

