# projects/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
]