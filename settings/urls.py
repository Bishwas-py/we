from django.urls import path
from.import views

urlpatterns=[
    path('', views.settings, name='settings'),
    path('add-class', views.addclass, name='addclass'),

]

