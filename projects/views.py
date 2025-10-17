# projects/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import Project, Milestone, Build
from tasks.models import Task
from bugs.models import Bug
from devlogs.models import DevLog

def home(request):
    projects = Project.objects.all()
    active_projects = projects.filter(status__in=['prototype', 'production', 'polish'])
    
    # Get recent activity
    recent_tasks = Task.objects.filter(
        status='completed',
        completed_date__gte=timezone.now() - timedelta(days=7)
    )[:5]
    
    recent_devlogs = DevLog.objects.all()[:3]
    open_bugs = Bug.objects.exclude(status='resolved')[:5]
    
    context = {
        'projects': projects,
        'active_projects': active_projects,
        'recent_tasks': recent_tasks,
        'recent_devlogs': recent_devlogs,
        'open_bugs': open_bugs,
    }
    return render(request, 'home.html', context)

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.task_set.all()
    
    # Task statistics
    task_stats = {
        'total': tasks.count(),
        'completed': tasks.filter(status='completed').count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'todo': tasks.filter(status='todo').count(),
    }
    
    # Recent activity
    recent_logs = project.devlog_set.all()[:5]
    open_bugs = project.bug_set.exclude(status='resolved')
    recent_builds = project.build_set.all()[:3]
    milestones = project.milestone_set.filter(completed=False)
    
    context = {
        'project': project,
        'tasks': tasks[:10],  # Show latest 10 tasks
        'task_stats': task_stats,
        'recent_logs': recent_logs,
        'open_bugs': open_bugs,
        'recent_builds': recent_builds,
        'milestones': milestones,
    }
    return render(request, 'projects/project_detail.html', context)

@login_required
def project_create(request):
    if request.method == 'POST':
        # Simple form handling without forms.py for now
        project = Project(
            name=request.POST['name'],
            code_name=request.POST.get('code_name', ''),
            description=request.POST.get('description', ''),
            genre=request.POST['genre'],
            engine=request.POST['engine'],
            status=request.POST.get('status', 'concept'),
            is_jam_game='is_jam_game' in request.POST,
            jam_name=request.POST.get('jam_name', ''),
        )
        project.save()
        messages.success(request, f"Project '{project.name}' created!")
        return redirect('project_detail', pk=project.pk)
    
    return render(request, 'projects/project_form.html', {'engines': Project.ENGINE_CHOICES, 'statuses': Project.STATUS_CHOICES})

@login_required
# projects/views.py - add these functions
def milestone_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    
    if request.method == 'POST':
        milestone = Milestone(
            project=project,
            name=request.POST['name'],
            description=request.POST.get('description', ''),
            due_date=request.POST['due_date'],
        )
        milestone.save()
        messages.success(request, "Milestone created!")
        return redirect('project_detail', pk=project.pk)
    
    context = {'project': project}
    return render(request, 'projects/milestone_form.html', context)

@login_required
def milestone_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    milestones = project.milestone_set.all()
    
    context = {
        'project': project,
        'milestones': milestones,
    }
    return render(request, 'projects/milestone_list.html', context)

@login_required
def build_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    builds = project.build_set.all()
    
    context = {
        'project': project,
        'builds': builds,
    }
    return render(request, 'projects/build_list.html', context)