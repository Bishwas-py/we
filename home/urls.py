from django.urls import path
from.import views, ajax_views

urlpatterns=[
    path('', views.home, name='home'),
    path('log-in', views.login, name='login'),
    path('register', views.register, name='register'),


    # Ajax Views that returns maximum days in BS month and today's date as well
    path('max-np-day', ajax_views.max_nepali_day, name='max_nepali_day'),
    path('today-date', ajax_views.todaydate, name='today')
]

