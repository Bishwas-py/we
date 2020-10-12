from django.shortcuts import render

# Create your views here.
def profile(request):
    username= request.session['username']
    password=request.session['password']
    return render(request, "settings/profile.html", {'stc':stdClass.objects.filter(username=username, password=password), 'sdata': schoolDetails.objects.get(username=username, password=password)})
