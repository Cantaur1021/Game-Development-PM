# tasks/admin.py

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'category', 'priority', 'status', 'assigned_to']
    list_filter = ['status', 'priority', 'category']
    search_fields = ['title', 'description']