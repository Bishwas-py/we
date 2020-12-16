from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from school.models import Class
from django.contrib.auth.models import User
from .models import School


# Register your models here.

class ClassInline(admin.TabularInline):
    model = Class

<<<<<<< HEAD
class UserAdmin(BaseUserAdmin):
  list_display = (
    'username','principal', 'submitted_date', 'school_name'
  )
  inlines = [
        ClassInline,
  ]


# admin.site.unregister(User)
admin.site.register(School, UserAdmin)
=======
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'principal', 'submitted_date', 'school_name'
    )


admin.site.register(School, CustomUserAdmin)

# Register your models here.

# admin.site.register(School)
>>>>>>> 2ead9db9503d20ce0112d399f05588fb12326618
