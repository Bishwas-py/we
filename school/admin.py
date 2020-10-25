from django.contrib import admin
from school.models import student_class
from accounts.models import school_details
# Register your models here.
class StudentClassAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': [
                                'class_list',
                                'connect_school',]}),)

    list_display = ('class_list','connect_school',)
admin.site.register(student_class, StudentClassAdmin)
