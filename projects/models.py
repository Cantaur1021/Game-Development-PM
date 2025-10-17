# projects/models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Project(models.Model):
    STATUS_CHOICES = [
        ('concept', '💭 Concept'),
        ('prototype', '🔨 Prototype'),
        ('production', '🚀 Production'),
        ('polish', '✨ Polish'),
        ('released', '🎮 Released'),
        ('shelved', '📦 Shelved'),
    ]
    
    ENGINE_CHOICES = [
        ('unity', 'Unity'),
        ('godot', 'Godot'),
        ('unreal', 'Unreal Engine'),
        ('gamemaker', 'GameMaker'),
        ('construct', 'Construct'),
        ('custom', 'Custom Engine'),
        ('web', 'Web (HTML5/JS)'),
    ]
    
    name = models.CharField(max_length=200)
    code_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=50)
    engine = models.CharField(max_length=20, choices=ENGINE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='concept')
    
    target_release = models.DateField(null=True, blank=True)
    actual_release = models.DateField(null=True, blank=True)
    
    repo_url = models.URLField(blank=True)
    itch_url = models.URLField(blank=True)
    steam_url = models.URLField(blank=True)
    
    is_jam_game = models.BooleanField(default=False)
    jam_name = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
    
    @property
    def progress_percentage(self):
        total_tasks = self.task_set.count()
        if total_tasks == 0:
            return 0
        completed_tasks = self.task_set.filter(status='completed').count()
        return int((completed_tasks / total_tasks) * 100)
    
    @property
    def open_bugs_count(self):
        return self.bug_set.exclude(status='resolved').count()

class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['due_date']
    
    def __str__(self):
        return f"{self.project.name} - {self.name}"

class Build(models.Model):
    PLATFORM_CHOICES = [
        ('windows', 'Windows'),
        ('mac', 'macOS'),
        ('linux', 'Linux'),
        ('webgl', 'WebGL'),
        ('android', 'Android'),
        ('ios', 'iOS'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    version = models.CharField(max_length=20)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    build_date = models.DateTimeField(auto_now_add=True)
    changelog = models.TextField()
    file_url = models.URLField(blank=True)
    file_size_mb = models.FloatField(null=True, blank=True)
    is_stable = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-build_date']
    
    def __str__(self):
        return f"{self.project.name} v{self.version} ({self.platform})"