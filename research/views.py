from django.shortcuts import render, get_object_or_404
from .models import ResearchProject, Researcher
from django.db.models import Count

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ResearcherForm, ResearchProjectForm

# Add a researcher
def add_researcher(request):
    if request.method == 'POST':
        form = ResearcherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('researcher_list')  # Redirect to researcher list
    else:
        form = ResearcherForm()
    return render(request, 'research/add_researcher.html', {'form': form})

# Add a research project
def add_project(request):
    if request.method == 'POST':
        form = ResearchProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect to project list
    else:
        form = ResearchProjectForm()
    return render(request, 'research/add_project.html', {'form': form})

# List all researchers
def researcher_list(request):
    researchers = Researcher.objects.all()
    return render(request, 'research/researcher_list.html', {'researchers': researchers})

# View a single researcher detail
def researcher_detail(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    return render(request, 'research/researcher_detail.html', {'researcher': researcher})

# Edit a researcher
def edit_researcher(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == 'POST':
        form = ResearcherForm(request.POST, instance=researcher)
        if form.is_valid():
            form.save()
            return redirect('researcher_list')
    else:
        form = ResearcherForm(instance=researcher)
    return render(request, 'research/edit_researcher.html', {'form': form})

# Delete a researcher
def delete_researcher(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == 'POST':
        researcher.delete()
        return redirect('researcher_list')
    return render(request, 'research/delete_researcher.html', {'researcher': researcher})

# List all research projects
def project_list(request):
    projects = ResearchProject.objects.all()
    researchers = Researcher.objects.all()
    data_points = ResearchProject.objects.values("title").annotate(
        researchers_count=Count("researchers")
    )
    context = [
        {
            'title': data['title'],
            'researchers_count': data['researchers_count']
        }
        for data in data_points
    ]
    return render(request, 'research/project_list.html', {'projects': projects,'context':context})


# View a single project detail
def project_detail(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    return render(request, 'research/project_detail.html', {'project':project})

# Edit a research project
def edit_project(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    if request.method == 'POST':
        form = ResearchProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ResearchProjectForm(instance=project)
    return render(request, 'research/edit_project.html', {'form': form})

# Delete a research project
def delete_project(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'research/delete_project.html', {'project': project})

