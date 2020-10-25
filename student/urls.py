from django.urls import path
from.import views

urlpatterns=[
    path('add-student', views.add_student, name='add_student'),
    path('student', views.student, name='student'),
    path('update_student/<ssname>', views.update_student, name='update_student'),
    path('delete/<ssname>', views.remove_student, name='remove_student'),

    path('test', views.test, name='test')
]

