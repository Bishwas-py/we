
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

# AD to BS
import adbs
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect


from accounts.models import School
from student.models import Student
from school.models import Class


# Create your views here.


def dashboard(request):
    class_data = Class.objects.filter(connect_school=request.user)
    student_data = Student.objects.filter(connect_school=request.user)
    required_dict = {
        'Class':class_data,
        'Student':student_data
    }
    return render(request, 'contents/dashboard.html', required_dict)


def log_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse("Logged in test")

        return render(request,'home/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if User exists
        school_user = authenticate(username=username, password=password)
        if school_user is not None:
            # Login user if user exists
            login(request, school_user)
            # messages.success(request, 'You are now logged in')
            return HttpResponse("Logged in")
        else:
            # Give error if user doesn't exist
            # messages.error(request, 'Invalid credentials')
            return HttpResponse("Faliure logged in")
    else:
        return render(request, 'home/login.html')


        
def register(request):

    if request.method == 'GET':
        return render(request, 'home/register.html')

    if request.method =='POST':
        school_name=request.POST['school_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        address = request.POST['address']
        principal = request.POST['principal']
        """   DATES    """
        year, month, day = request.POST['year'], request.POST['month'], request.POST['day']
        
        from modules.date_works import convert
        dates = convert(year, month, day)
        nepali_established_date =  dates['np']
        established_date = dates['en']

        student_number = request.POST['student_number']
        ip = request.META.get('REMOTE_ADDR', None)

        is_email_used = School.objects.filter(email=email).exists()
        is_username_used = School.objects.filter(email=username).exists()


        if is_email_used and is_username_used:
            error_msg = f'{username} and {email} is already used for sign in.'
            return render(request, 'home/register.html', {'error_msg':error_msg})

        if is_email_used:
            error_msg = f'{email} is already used for sign in.'
            return render(request, 'home/register.html', {'error_msg':error_msg})

        if is_username_used:
            error_msg = f'{username} is already used for sign in.'
            return render(request, 'home/register.html', {'error_msg':error_msg})

        school_user = School.objects.create_user(
            username=username,
            password=password,
            email=email,
            school_name=school_name,
            principal=principal,
            address=address,
            established_date=established_date,
            nepali_established_date=nepali_established_date,
            student_number=student_number,
            user_ip=ip
        )
        school_user.save()
        login(request, school_user)
        return redirect('/accounts/dashboard')
    

def user_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def delete_account(request):
    confirm_password = request.POST['delpassword']
    if confirm_password == change_needed_school_data.password:
        for i in range(0,len(change_needed_student_data)):
            change_needed_student_data = Student.objects.get(
                username=School.objects.get(username=username),
                student_short_name=change_needed_student_data[i].student_short_name
            )

            change_needed_student_data.stpht.delete(save=True)
            change_needed_student_data.delete()

        change_needed_school_data.delete()
        return redirect('accounts/logout')
    else:
        #stc == > Class
        render_required_dictonary = {
            'Class':Class.objects.filter(
                username=School.objects.get(username=username),
                password=password
            ),
            'wpsd':'Wrong Password...',
            'Student': Student.objects.get(
                username=request.session['username']
                )
        }
        return render(request, "contents/profile.html", render_required_dictonary)


def update(request):
    #using ajax
    username=request.session['username']
    password=request.session['password']

    change_needed_school_data = School.objects.get(
        username=School.objects.get(username=username),
        password=password
    )
    change_needed_student_data = Student.objects.filter(
        username=School.objects.get(username=username),
    )

    # try:
    principal=request.POST.get('name')
    change_needed_school_data.principal = principal
    change_needed_school_data.save()
    # except:
    #     None
    
    try:
        address=request.POST['address']
        change_needed_school_data.address = address
        change_needed_school_data.save()
    except:
        None

    try:
        password=request.POST['password']
        change_needed_school_data.password = password
        change_needed_school_data.save()
        request.session['password'] = password

    except:
        None
    return redirect('profile')


def log_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    context = {
        'Class': Class.objects.filter(
            connect_school=request.user
        ),
    }
    return render(request, "contents/profile.html", context)


def log_in(request):
    if request.method == 'GET':
        return render(request, 'home/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        if username is None or password is None:
            messages.error(request, "Wrong username or password")
            return HttpResponseRedirect(reverse('log_in'))

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))

