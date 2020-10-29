from django.urls import path
from.import views

urlpatterns=[
    path('', views.student, name='student'),
    path('add-student', views.add_student, name='add_student'),
    path('student', views.student, name='student'),
    path('update_student/<short_name>', views.update_student, name='update_student'),
    path('delete/<short_name>', views.delete, name='delete'),

    path('profile/<short_name>', views.student_profile, name='student_profile')
]

