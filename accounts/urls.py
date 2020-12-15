from django.urls import path
from.import views

urlpatterns = [
    path('log-in', views.log_in, name='log_in'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout,name='logout'),
    path('update', views.update, name='update'),
    path('dashboard', views.dashboard, name='dashboard'),

]

























