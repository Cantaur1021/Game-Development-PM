# assets/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Asset
from projects.models import Project

# @login_required  # Uncomment when auth is set up
def asset_upload(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    
    if request.method == 'POST':
        asset = Asset(
            project=project,
            name=request.POST['name'],
            asset_type=request.POST['asset_type'],
            status=request.POST.get('status', 'concept'),
            description=request.POST.get('description', ''),
            license=request.POST.get('license', ''),
            source_url=request.POST.get('source_url', ''),
        )
        if 'file' in request.FILES:
            asset.file = request.FILES['file']
        if 'thumbnail' in request.FILES:
            asset.thumbnail = request.FILES['thumbnail']
        asset.save()
        messages.success(request, f"Asset '{asset.name}' uploaded!")
        return redirect('asset_list', project_pk=project.pk)
    
    context = {
        'project': project,
        'asset_types': Asset.TYPE_CHOICES,
        'statuses': Asset.STATUS_CHOICES,
    }
    return render(request, 'assets/asset_upload.html', context)

def asset_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    assets = project.asset_set.all()
    
    context = {
        'project': project,
        'assets': assets,
    }
    return render(request, 'assets/asset_list.html', context)