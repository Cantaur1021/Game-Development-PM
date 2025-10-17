# config/urls.py (updated)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    path('devlogs/', include('devlogs.urls')),
    path('bugs/', include('bugs.urls')),
    path('assets/', include('assets.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)