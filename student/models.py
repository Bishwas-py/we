from django.db import models
from django.utils import timezone
import nepali_datetime
from school.models import Class
from accounts.models import School
# Create your models here.
class Student(models.Model):
    connect_school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    # School = models.ForeignKey(schoolDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    gender_choices = [('m','Male'), ('f','Female'),('o','Others')]
    gender = models.CharField(max_length=9, choices=gender_choices, default='1')

    ethnic_groups = [('brah','Brahmin'), ('cht','Chhetri'), ('jj', 'Janajati'), ('dl', 'Dalit'), ('md','Madhesi')]
    ethnicity = models.CharField(max_length=9, choices=ethnic_groups, default='1')
    short_name = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=False)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    father = models.CharField(max_length=150, null=True)
    mother = models.CharField(max_length=150, null=True)
    fam_occupation = models.CharField(max_length=150, null=True)
    nepali_admission_date = models.CharField(default=str(nepali_datetime.date.today()), max_length=150, null=True)
    eng_admission_date = models.CharField(default=timezone.now, max_length=150, null=True)
    nepali_dob_date = models.CharField(default=str(nepali_datetime.date.today()), max_length=150, null=True)
    eng_dob_date = models.CharField(default=timezone.now, max_length=150, null=True)
    phone_number = models.CharField(max_length=95, null=True)
    photo = models.ImageField(max_length=500, upload_to='', default='/media/web/')

    #(""), upload_to=None, height_field=None, width_field=None,
    
    def __str__(self):
        return self.name
#datetime.datetime(2020, 6, 25, 2, 33, 57, 858649, tzinfo=<UTC>)