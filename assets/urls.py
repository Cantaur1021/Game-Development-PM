# assets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:project_pk>/', views.asset_upload, name='asset_upload'),
    path('project/<int:project_pk>/', views.asset_list, name='asset_list'),
]