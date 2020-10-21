from django.urls import path
from.import views

urlpatterns=[
    path('profile', views.profile, name='profile'),
    path('add-class', views.addclass, name='add_class'),
    path('auto-class-create', views.automatic_class, name='auto_class')
    
]