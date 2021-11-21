from django.shortcuts import render, redirect
from .forms import CreateProjectForm, ProjectForm
from .models import Project 

# Create your views here.
# I can use Views as functions or classes. Using the function option,
projects_list = [
    {
        "id": 1,
        "title": "Portfolio Website",
        "description": "A portfolio website I gotta make.",
    },
    {
        "id": 2,
        "title": "Informed",
        "description": "A mobile app to see weather forecast and news.",
    },
    {
        "id": 3,
        "title": "Maestro X",
        "description": "An application to improve self-discipline and productivity.",
    },
]


def projects(request):
    my_projects = Project.objects.all()
    context = {"projects": my_projects}
    return render(request, "app_projects/projects.html", context)


def project(request, pk):
    selected_project = Project.objects.get(id=pk)
    context = {"project": selected_project}
    return render(request, "app_projects/project.html", context)


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, "app_projects/project-form.html", context)

def edit_project(request,pk):
    selected_project = Project.objects.get(id=pk)
    form = ProjectForm(instance=selected_project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=selected_project)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, "app_projects/project-form.html", context)

def delete_project(request,pk):
    selected_project = Project.objects.get(id=pk)
    context = {"project": selected_project}

    if request.method == 'POST':
        selected_project.delete()
        return redirect('/')
    
    return render(request, "app_projects/delete.html", context)
