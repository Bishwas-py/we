from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
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

class Subject(models.Model):
    connect_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=False)
    subject = models.ManyToManyField(SubjectsList)



@receiver(pre_save, sender=Subject)
def on_save(sender, instance, **kwargs):
    subjects_data = requests.get(instance.subjects)
    instance.subjects = subjects_data

# object.m2mfield.add(*items)   