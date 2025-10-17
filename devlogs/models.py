# devlogs/models.py

from django.db import models
from projects.models import Project
import markdown2

class DevLog(models.Model):
    MOOD_CHOICES = [
        ('frustrated', '😤 Frustrated'),
        ('stuck', '🤔 Stuck'),
        ('neutral', '😐 Neutral'),
        ('productive', '😊 Productive'),
        ('flow', '🔥 In Flow'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)
    
    work_done = models.TextField(help_text="What did you accomplish? (Markdown supported)")
    blockers = models.TextField(blank=True, help_text="What's blocking progress?")
    next_steps = models.TextField(blank=True, help_text="What's next?")
    
    hours_worked = models.FloatField(default=0)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default='neutral')
    
    screenshot = models.ImageField(upload_to='devlogs/%Y/%m/', blank=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.project.name} - {self.date}"
    
    def work_done_html(self):
        return markdown2.markdown(self.work_done)
    
    def blockers_html(self):
        return markdown2.markdown(self.blockers)
    
    def next_steps_html(self):
        return markdown2.markdown(self.next_steps)