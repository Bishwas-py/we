from django.http import JsonResponse

from .models import Class
def automatic_class(request):
    # already_created = []
    if request.method == 'POST':
        required_classes = ['Nursery','L.K.G','U.K.G','Kindergarten']+["Class "+ str(i) for i in range(1, 11)]
        array_of_class = []
        if Class.objects.filter(connect_school=request.user):
            required_dict = {
                'success_value':'primary',
                'success_message':f"Classes are already created.",
                'success_body':f"The class are already created. You can procced to next step.",
                'success_remarks':'Success'
                }
            return JsonResponse(required_dict)
        else:
            for class_data in required_classes:
                array_of_class.append(Class(
                    connect_school=request.user,
                    class_list=class_data
                ))
            Class.objects.bulk_create(array_of_class)
            required_dict = {
                'success_value':'success',
                'success_message':f"Classes created automatically",
                'success_body':f"The class are created automatically. You can now procced to next step.",
                'success_remarks':'Success'
                }
            return JsonResponse(required_dict)
    else:
        return HttpResponse(0)