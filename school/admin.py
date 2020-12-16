from django.contrib import admin
from school.models import Class , Subject
from accounts.models import School
# Register your models here.
class StudentClassAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': [
                                'class_list',
                                'connect_school',]}),)

    list_display = ('class_list','connect_school',)
admin.site.register(Class, StudentClassAdmin)

class ClassInline(admin.TabularInline):
    model = Class

class SchoolAdmin(admin.ModelAdmin):
    inlines = [
        ClassInline,
    ]

# class StudentSubjectAdmin(admin.ModelAdmin):
#     fieldsets = ((None, {'fields': [
#                                 'subjects',
#                                 'connect_class',]}),)

#     list_display = ('class_list','connect_class',)
# admin.site.register(Subject, StudentSubjectAdmin)
admin.site.register(Subject)