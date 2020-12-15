from django.urls import path
from.import views

urlpatterns=[
    path('', views.home, name='home'),
    path('log-in', views.login, name='login'),
    path('register', views.register, name='register'),
    path('max-np-day', views.max_nepali_day, name='max_nepali_day'),
    path('today-date', views.todaydate, name='today'),
    path('website', views.website, name='website')
]

