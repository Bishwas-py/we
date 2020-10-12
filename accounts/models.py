from django.db import models
from django.utils import timezone
import nepali_datetime

# from django.contrib.auth.models import User
# Create your models here.

class school_details(models.Model):
    school_name = models.CharField(max_length=50)
    email = models.CharField(max_length=95)
    submitted_date = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=100)
    principal = models.CharField(max_length=150, default='')
    address = models.CharField(max_length=100, default='Nepal')
    established_date = models.CharField(default=timezone.now, max_length=95)
    nepali_established_date = models.CharField(default=str(nepali_datetime.date.today()), max_length=95)
    student_number = models.IntegerField(default=0) #number of student
    school_website = models.URLField(max_length=200, default='')
    password = models.CharField(max_length=95)
    user_ip = models.CharField(max_length=95)
    logo = models.ImageField(max_length=500, upload_to='', default='/media/web/your-logo-here.png')

    def __str__(self):
        return self.school_name