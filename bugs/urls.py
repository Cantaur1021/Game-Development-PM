# bugs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:project_pk>/', views.bug_create, name='bug_create'),
    path('project/<int:project_pk>/', views.bug_list, name='bug_list'),
    path('<int:pk>/', views.bug_detail, name='bug_detail'),
]