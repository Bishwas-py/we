from django.contrib import admin
from school.models import Class
from accounts.models import School
# Register your models here.
class StudentClassAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': [
                                'class_list',
                                'connect_school',]}),)

    list_display = ('class_list','connect_school',)
admin.site.register(Class, StudentClassAdmin)
