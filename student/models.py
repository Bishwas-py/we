from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import nepali_datetime
from accounts.models import School
from school.models import Class, Subject, MarksReport

# Create your models here.
class Student(models.Model):
    connect_school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    # School = models.ForeignKey(schoolDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    gender_choices = [('m', 'Male'), ('f', 'Female'), ('o', 'Others')]
    gender = models.CharField(max_length=9, choices=gender_choices, default='1')
    roll_num = models.IntegerField(null=True, blank=True)

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
    admission_date = models.DateField(default=timezone.now, max_length=150, null=True)

    nepali_dob_date = models.CharField(default=str(nepali_datetime.date.today()), max_length=150, null=True)    
    eng_dob_date = models.CharField(default=timezone.now, max_length=150, null=True)
    dob_date = models.DateField(default=timezone.now, max_length=150, null=True)
    
    phone_number = models.CharField(max_length=95, null=True)
    photo = models.ImageField(max_length=500, upload_to='', default='/media/web/')

    subject = models.ManyToManyField(Subject)
    marks_report = models.ForeignKey(MarksReport, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Student)
def populate_roll_num(sender, instance, created, **kwargs):
    if created:
        instance.roll_num = instance.id
        instance.save()
