# tasks/models.py

from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('programming', '💻 Programming'),
        ('art_2d', '🎨 2D Art'),
        ('art_3d', '🎮 3D Modeling'),
        ('animation', '🏃 Animation'),
        ('audio_music', '🎵 Music'),
        ('audio_sfx', '🔊 Sound Effects'),
        ('level_design', '🗺️ Level Design'),
        ('game_design', '🎲 Game Design'),
        ('ui_ux', '📱 UI/UX'),
        ('narrative', '📝 Story/Narrative'),
        ('marketing', '📢 Marketing'),
        ('bugs', '🐛 Bug Fixes'),
        ('polish', '✨ Polish/Juice'),
        ('optimization', '⚡ Performance'),
    ]
    
    PRIORITY_CHOICES = [
        ('blocker', '🔴 Game Breaking'),
        ('critical', '🟠 Critical'),
        ('major', '🟡 Major'),
        ('minor', '🟢 Minor'),
        ('polish', '🔵 Nice to Have'),
    ]
    
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('review', 'In Review'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='minor')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    estimated_hours = models.FloatField(null=True, blank=True)
    actual_hours = models.FloatField(null=True, blank=True)
    
    due_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-priority', '-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"