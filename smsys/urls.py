from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('settings/', include('settings.urls')),
    path('student/', include('student.urls')),
    path('school/', include('school.urls'))
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#EXAMPLE: path('accounts/', include('accounts.urls'))
