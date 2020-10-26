from django.db import models
from accounts.models import School

class Class(models.Model):
    connect_school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    class_list = models.CharField(max_length=95)
    def __str__(self):
            return self.class_list
    