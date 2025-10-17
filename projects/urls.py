# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    path('<int:project_pk>/milestones/', views.milestone_list, name='milestone_list'),
    path('<int:project_pk>/milestones/create/', views.milestone_create, name='milestone_create'),
    path('<int:project_pk>/builds/', views.build_list, name='build_list'),
]