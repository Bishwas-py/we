from django.db import models
from accounts.models import school_details

class student_class(models.Model):
    connect_school = models.ForeignKey(school_details, on_delete=models.CASCADE, null=True)
    class_list = models.CharField(max_length=95)
    def __str__(self):
            return self.class_list
    