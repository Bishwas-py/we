# from accounts.models import School
# from django.conf import settings

def school_context(request):
    school = request.user

    return {'School':school}