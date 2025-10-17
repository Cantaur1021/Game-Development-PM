# devlogs/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DevLog
from projects.models import Project

@login_required
def devlog_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    
    if request.method == 'POST':
        devlog = DevLog(
            project=project,
            title=request.POST.get('title', ''),
            work_done=request.POST['work_done'],
            blockers=request.POST.get('blockers', ''),
            next_steps=request.POST.get('next_steps', ''),
            hours_worked=float(request.POST.get('hours_worked', 0)),
            mood=request.POST.get('mood', 'neutral'),
        )
        if 'screenshot' in request.FILES:
            devlog.screenshot = request.FILES['screenshot']
        devlog.save()
        messages.success(request, "Dev log added!")
        return redirect('project_detail', pk=project.pk)
    
    context = {
        'project': project,
        'moods': DevLog.MOOD_CHOICES,
    }
    return render(request, 'devlogs/devlog_form.html', context)

# devlogs/views.py - add this function
def devlog_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    devlogs = project.devlog_set.all()
    
    context = {
        'project': project,
        'devlogs': devlogs,
    }
    return render(request, 'devlogs/devlog_list.html', context)