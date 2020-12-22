from django.urls import path
from school import views, ajax_views

urlpatterns=[
    path('add-class', views.add_class, name='add_class'),
    path('auto-class-create', ajax_views.automatic_class, name='auto_class'),
    path('create-subjects', views.add_subject, name='add_subject'),
]