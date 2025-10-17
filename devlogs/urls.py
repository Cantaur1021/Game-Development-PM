# devlogs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('project/<int:project_pk>/', views.devlog_list, name='devlog_list'),
    path('create/<int:project_pk>/', views.devlog_create, name='devlog_create'),
]