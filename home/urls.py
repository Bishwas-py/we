from django.urls import path
from.import views, ajax_views

urlpatterns=[
    path('', views.home, name='home'),
    path('log-in', views.login, name='login'),
<<<<<<< HEAD
    path('register', views.register, name='register'),


    # Ajax Views that returns maximum days in BS month and today's date as well
    path('max-np-day', ajax_views.max_nepali_day, name='max_nepali_day'),
    path('today-date', ajax_views.todaydate, name='today')
=======
    # path('register', views.register, name='register'),
    path('max-np-day', views.max_nepali_day, name='max_nepali_day'),
    path('today-date', views.todaydate, name='today'),
    path('website', views.website, name='website')
>>>>>>> 2ead9db9503d20ce0112d399f05588fb12326618
]

