# Create a new file: projects/context_processors.py
from .models import Project

def all_projects(request):
    return {
        'all_projects': Project.objects.all()[:10]  # Limit to 10 most recent
    }