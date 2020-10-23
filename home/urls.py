from django.urls import path
from.import views

urlpatterns=[
    path('', views.home, name='home'),
    path('max-np-day', views.max_nepali_day, name='max_nepali_day'),
    path('today-date', views.todaydate, name='today')
]

