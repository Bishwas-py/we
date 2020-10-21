from django.shortcuts import render, redirect
from accounts.models import school_details
from student.models import student_details
from school.models import student_class
import adbs
# Create your views here.
def dashboard(request):
    username = request.session['username']
    password = request.session['password']
    
    school_Details = school_details.objects.get(username=username, password=password)
    try:
        student_Class = school_details.objects.get(username=school_Details)
    except:
        student_Class = None
    try:
        student_Details = student_details.objects.get(username=school_Details)
    except:
        student_Details = None
    required_dict = {
        'school_details':school_Details,
        'student_class':student_Class,
        'student_details':student_Details
    }

    return render(request, 'themes/dashboard.html', required_dict )        


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
            change_needed_student_data = student_details.objects.get(
                username=school_details.objects.get(username=username),
                student_short_name=change_needed_student_data[i].student_short_name
            )

            change_needed_student_data.stpht.delete(save=True)
            change_needed_student_data.delete()

        change_needed_school_data.delete()
        return redirect('accounts/logout')
    else:
        #stc == > student_class
        render_required_dictonary = {
            'student_class':student_class.objects.filter(
                username=school_details.objects.get(username=username),
                password=password
            ),
            'wpsd':'Wrong Password...',
            'student_details': student_details.objects.get(
                username=request.session['username']
                )
        }
        return render(request, "themes/profile.html", render_required_dictonary)


def update(request):
    #using ajax
    username=request.session['username']
    password=request.session['password']
    print('Username', username, password)

    change_needed_school_data = school_details.objects.get(
        username=school_details.objects.get(username=username),
        password=password
    )
    change_needed_student_data = student_details.objects.filter(
        username=school_details.objects.get(username=username),
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


def logout(request):
     request.session.delete()
     return redirect('home')


def profile(request):
    username = request.session['username']
    password = request.session['password']
    render_required_dictonary = {
    'student_class':student_class.objects.filter(
        username=school_details.objects.get(username=username)
    ),
    'school_details': school_details.objects.get(
        username=request.session['username'],
        password=request.session['password'])
}
    return render(request, "themes/profile.html", render_required_dictonary)


def log_in(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user_logged = school_details.objects.filter(username=username,password=password)
            if not user_logged:
                return render(request, "home/home.html", {'error': 'Username or Password is incorrect...'})
            else:
                print('I am here')
                request.session['username'] = username
                request.session['password'] = password
                return redirect('dashboard')
    else:
        if request.session.has_key('username') and request.session.has_key('password'):
            return redirect('home')
        else:
            return render(request, 'home/home.html', {'signin':f'Please sign in to surf DASHBOARD.'})


def sign_in(request):
        #register
    if request.session.has_key('username') and request.session.has_key('password'):
            return redirect('home')
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
        school_website = request.POST['school_website']
        ip = user_ip_address(request)
        
        try:
            used_account_filter = school_details.objects.filter(email=email, username=school_details.objects.get(username=username))
            if not used_account_filter.email and not used_account_filter.username:
                error_msg = f'{username} and {email} is already used for sign in.'
                return render(request, 'home.html', {'used_or_not':error_msg})

            if not used_account_filter.email:
                error_msg = f'{email} is already used for sign in.'
                return render(request, 'home.html', {'used_or_not':error_msg})

            if not used_account_filter.username:
                error_msg = f'{username} is already used for sign in.'
                return render(request, 'home.html', {'used_or_not':error_msg})

        except:
            None
        
        
        request.session['username'] = username
        request.session['password'] = password
        
        school_data = school_details(
            username=username,
            password=password,
            email=email,
            school_name=school_name,
            principal=principal,
            address=address,
            established_date=established_date,
            nepali_established_date=nepali_established_date,
            student_number=student_number,
            school_website=school_website,
            user_ip=ip
        )
        school_data.save()
        return redirect('/accounts/dashboard')
    else:
        return render(request, 'home/home.html', {'signin':f'Please sign in to surf DASHBOARD.'})


