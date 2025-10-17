# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:project_pk>/', views.task_create, name='task_create'),
    path('<int:pk>/update-status/', views.task_update_status, name='task_update_status'),
]