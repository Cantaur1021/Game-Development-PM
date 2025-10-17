# assets/models.py

from django.db import models
from projects.models import Project

class Asset(models.Model):
    TYPE_CHOICES = [
        ('sprite', '🖼️ Sprite'),
        ('texture', '🎨 Texture'),
        ('model_3d', '🎮 3D Model'),
        ('audio_music', '🎵 Music'),
        ('audio_sfx', '🔊 Sound Effect'),
        ('animation', '🏃 Animation'),
        ('shader', '✨ Shader'),
        ('font', '🔤 Font'),
        ('document', '📄 Document'),
    ]
    
    STATUS_CHOICES = [
        ('concept', 'Concept'),
        ('wip', 'Work in Progress'),
        ('review', 'Needs Review'),
        ('final', 'Final'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='concept')
    
    file = models.FileField(upload_to='assets/%Y/%m/', blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/', blank=True)
    
    description = models.TextField(blank=True)
    license = models.CharField(max_length=100, blank=True, help_text="e.g., CC0, Purchased, Original")
    source_url = models.URLField(blank=True, help_text="If from asset store or external source")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_asset_type_display()})"