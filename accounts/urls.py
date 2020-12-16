from django.urls import path
from.import views

urlpatterns = [
    path('log-in', views.log_in, name='log_in'),
    path('logout', views.log_out,name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('update', views.update, name='update'),
    path('dashboard', views.dashboard, name='dashboard'),

]

























