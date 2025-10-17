# bugs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bug
from projects.models import Project, Build

# @login_required  # Uncomment when auth is set up
def bug_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    builds = project.build_set.all()
    
    if request.method == 'POST':
        bug = Bug(
            project=project,
            title=request.POST['title'],
            description=request.POST['description'],
            reproduction_steps=request.POST['reproduction_steps'],
            expected_behavior=request.POST['expected_behavior'],
            actual_behavior=request.POST['actual_behavior'],
            severity=request.POST['severity'],
            status=request.POST.get('status', 'new'),
            level_scene=request.POST.get('level_scene', ''),
        )
        if request.POST.get('build_version'):
            bug.build_version_id = request.POST['build_version']
        if 'screenshot' in request.FILES:
            bug.screenshot = request.FILES['screenshot']
        if request.user.is_authenticated:
            bug.reported_by = request.user
        bug.save()
        messages.success(request, "Bug reported successfully!")
        return redirect('bug_list', project_pk=project.pk)
    
    context = {
        'project': project,
        'builds': builds,
        'severities': Bug.SEVERITY_CHOICES,
        'statuses': Bug.STATUS_CHOICES,
    }
    return render(request, 'bugs/bug_form.html', context)

def bug_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    bugs = project.bug_set.all()
    
    context = {
        'project': project,
        'bugs': bugs,
    }
    return render(request, 'bugs/bug_list.html', context)

def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    context = {'bug': bug}
    return render(request, 'bugs/bug_detail.html', context)