from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import School
# Register your models here.


class CustomUserAdmin(UserAdmin):
  list_display = (
    'username','principal', 'submitted_date', 'school_name'
  )


admin.site.register(School, CustomUserAdmin)
# Register your models here.

# admin.site.register(School)