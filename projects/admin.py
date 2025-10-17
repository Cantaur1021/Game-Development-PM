# projects/admin.py

from django.contrib import admin
from .models import Project, Milestone, Build

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'engine', 'genre', 'created_at']
    list_filter = ['status', 'engine', 'is_jam_game']
    search_fields = ['name', 'description']

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'due_date', 'completed']
    list_filter = ['completed', 'due_date']

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ['project', 'version', 'platform', 'build_date', 'is_stable']
    list_filter = ['platform', 'is_stable']