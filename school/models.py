from django.db import models
from accounts.models import School


class Class(models.Model):
    connect_school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    class_list = models.CharField(max_length=95)
    def __str__(self):
            return self.class_list

class Subject(models.Model):
    connect_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    subjects = models.CharField(max_length=95, null=True)
    def __str__(self):
        return self.subjects