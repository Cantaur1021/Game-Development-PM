# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from projects.models import Project

@login_required
def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    
    if request.method == 'POST':
        task = Task(
            project=project,
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            category=request.POST['category'],
            priority=request.POST['priority'],
            status=request.POST.get('status', 'todo'),
            estimated_hours=request.POST.get('estimated_hours') or None,
        )
        if request.POST.get('assigned_to'):
            task.assigned_to_id = request.POST['assigned_to']
        task.save()
        messages.success(request, f"Task '{task.title}' created!")
        return redirect('project_detail', pk=project.pk)
    
    context = {
        'project': project,
        'categories': Task.CATEGORY_CHOICES,
        'priorities': Task.PRIORITY_CHOICES,
        'statuses': Task.STATUS_CHOICES,
    }
    return render(request, 'tasks/task_form.html', context)

@login_required
def task_update_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST['status']
        task.status = new_status
        if new_status == 'completed':
            task.completed_date = timezone.now().date()
        task.save()
        messages.success(request, f"Task status updated!")
    
    return redirect('project_detail', pk=task.project.pk)

@login_required
# tasks/views.py - add this function
def task_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    tasks = project.task_set.all()
    
    context = {
        'project': project,
        'tasks': tasks,
    }
    return render(request, 'tasks/task_list.html', context)