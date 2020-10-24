from django.db import models
from django.utils import timezone
import nepali_datetime
from school.models import student_class
from accounts.models import school_details
# Create your models here.
class student_details(models.Model):
    connect_school = models.ForeignKey(school_details, on_delete=models.CASCADE, null=True)
    # school_details = models.ForeignKey(schoolDetails, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=150, null=True)
    gender_choices = [('m','Male'), ('f','Female'),('o','Others')]
    gender = models.CharField(max_length=9, choices=gender_choices, default='1')

    ethnic_groups = [('brah','Brahmin'), ('cht','Chhetri'), ('jj', 'Janajati'), ('dl', 'Dalit'), ('md','Madhesi')]
    ethnicity = models.CharField(max_length=9, choices=ethnic_groups, default='1')
    student_short_name = models.CharField(max_length=150, null=True)
    student_address = models.CharField(max_length=150, null=False)
    student_class = models.ForeignKey(student_class, on_delete=models.CASCADE, null=True)
    student_father = models.CharField(max_length=150, null=True)
    student_mother = models.CharField(max_length=150, null=True)
    student_fam_occupation = models.CharField(max_length=150, null=True)
    student_nepali_admission_date = models.CharField(default=str(nepali_datetime.date.today()), max_length=150, null=True)
    student_eng_admission_date = models.CharField(default=timezone.now, max_length=150, null=True)
    student_nepali_dob_date = models.CharField(default=str(nepali_datetime.date.today()), max_length=150, null=True)
    student_eng_dob_date = models.CharField(default=timezone.now, max_length=150, null=True)
    student_phone_number = models.CharField(max_length=95, null=True)
    student_photo = models.ImageField(max_length=500, upload_to='', default='/media/web/')

    #(""), upload_to=None, height_field=None, width_field=None,
    
    def __str__(self):
        return self.student_name
#datetime.datetime(2020, 6, 25, 2, 33, 57, 858649, tzinfo=<UTC>)