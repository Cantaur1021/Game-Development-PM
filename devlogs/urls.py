# devlogs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:project_pk>/', views.devlog_create, name='devlog_create'),
]