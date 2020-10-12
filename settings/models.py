from django.db import models
from accounts.models import school_details

# Create your models here.
class student_class(models.Model):
    username = models.ForeignKey(school_details, on_delete=models.CASCADE, null=True)
    class_list = models.CharField(max_length=95)
    def __str__(self):
            return self.class_list