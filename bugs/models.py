# bugs/models.py

from django.db import models
from django.contrib.auth.models import User
from projects.models import Project, Build

class Bug(models.Model):
    SEVERITY_CHOICES = [
        ('blocker', '🔴 Blocker'),
        ('critical', '🟠 Critical'),
        ('major', '🟡 Major'),
        ('minor', '🟢 Minor'),
        ('trivial', '⚪ Trivial'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('wont_fix', "Won't Fix"),
        ('duplicate', 'Duplicate'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    reproduction_steps = models.TextField(help_text="Steps to reproduce the bug")
    expected_behavior = models.TextField()
    actual_behavior = models.TextField()
    
    level_scene = models.CharField(max_length=100, blank=True, help_text="Which level or scene?")
    build_version = models.ForeignKey(Build, on_delete=models.SET_NULL, null=True, blank=True)
    
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='minor')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reported_bugs')
    
    screenshot = models.ImageField(upload_to='bugs/%Y/%m/', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-severity', '-created_at']
    
    def __str__(self):
        return f"[{self.get_severity_display()}] {self.title}"