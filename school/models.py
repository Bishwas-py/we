from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from accounts.models import School


class Class(models.Model):
    create_class = ['Nursery','L.K.G','U.K.G','Kindergarten']+["Class "+ str(i) for i in range(1, 11)]
    connect_school = models.ForeignKey(School, on_delete=models.CASCADE, null=False)
    class_list = models.CharField(max_length=95)
    def __str__(self):
            return self.class_list
    
    # def auto_class_creation(self, *args, **kwargs):
    #     create_class = ['Nursery','L.K.G','U.K.G','Kindergarten']+["Class "+ str(i) for i in range(1, 11)]
    #     for 


class SubjectsList(models.Model):
    sub = models.CharField(max_length=105)

    def __str__(self):
        return self.sub

class Subject(models.Model):
    connect_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=False)
    subject = models.ManyToManyField(SubjectsList)

    def __str__(self):
        return f"{str(self.id)}: {self.connect_class}"
