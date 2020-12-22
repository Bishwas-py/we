from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from accounts.models import School
#
# from student.models import Student


class Class(models.Model):
    create_class = ['Nursery', 'L.K.G', 'U.K.G', 'Kindergarten']+["Class " + str(i) for i in range(1, 11)]
    connect_school = models.ForeignKey(School, on_delete=models.CASCADE, null=False)
    class_name = models.CharField(max_length=95)

    def __str__(self):
            return self.class_name


class SubjectsList(models.Model):
    sub = models.CharField(max_length=105)
    full_marks = models.IntegerField(null=True)
    pass_marks = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.sub}: {self.id}'


class MarksReport(models.Model):
    subject = models.ForeignKey(SubjectsList, on_delete=models.CASCADE, null=True)
    obtained_marks = models.IntegerField(null=True)


@receiver(pre_save, sender=MarksReport)
def populate_full_pass_marks(sender, instance, *args, **kwargs):
    marks_report = MarksReport.objects.filter(subject=instance.subject)[-1]
    if marks_report:
        instance.full_marks = marks_report.full_marks
        instance.pass_marks = marks_report.pass_marks
        instance.save()


def populate_pass_marks(sender, instance, *args, **kwargs):
    if not MarksReport.objects.filter(subject=instance.subject)[-1]:
        instance.pass_marks = int(instance.full_marks * (40 / 100))
        instance.save()


class Subject(models.Model):
    connect_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=False)
    subject = models.ManyToManyField(SubjectsList)

    def __str__(self):
        return f"{str(self.id)}: {self.connect_class}"