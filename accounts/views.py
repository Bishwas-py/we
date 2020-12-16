from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from accounts.models import School
from student.models import Student
from school.models import Class
from .forms import LoginForm
import adbs
# Create your views here.


def dashboard(request):
    username = request.session['username']
    password = request.session['password']
    Class = School.objects.get(username=request.user)
    required_dict = {
        'Class':Class,
        'Student':Student
    }

    return render(request, 'themes/dashboard.html', required_dict )        



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
        try:
            used_account_filter = School.objects.filter(email=email, username=School.objects.get(username=username))
            if not used_account_filter.email and not used_account_filter.username:
                error_msg = f'{username} and {email} is already used for sign in.'
                return render(request, 'home.html', {'error_msg':error_msg})

            if not used_account_filter.email:
                error_msg = f'{email} is already used for sign in.'
                return render(request, 'home.html', {'error_msg':error_msg})

            if not used_account_filter.username:
                error_msg = f'{username} is already used for sign in.'
                return render(request, 'home.html', {'error_msg':error_msg})

        except:
            None
        
        
        request.session['username'] = username
        request.session['password'] = password
        
        school_data = School.objects.create_user(
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
        school_data.save()
        return redirect('/accounts/dashboard')
    

def user_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def delete_account(request):
    confirm_password=request.POST['delpassword']
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
        return render(request, "themes/profile.html", render_required_dictonary)


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
    render_required_dictonary = {
    'Class':Class.objects.filter(
        username=School.objects.get(username=username)
    ),
    'School': School.objects.get(
        username=request.session['username'],
        password=request.session['password'])
}
    return render(request, "themes/profile.html", render_required_dictonary)


