from django.contrib import admin
from school.models import student_class
from accounts.models import school_details
# Register your models here.
# class StudentClassAdmin(admin.ModelAdmin):
#     fieldsets = ((None, {'fields': [
#                                 'connect_school',
#                                 'class_list',]}),)

#     list_display = ('connect_school', 'class_list',)
# admin.site.register(student_class, StudentClassAdmin)
admin.site.register(student_class)