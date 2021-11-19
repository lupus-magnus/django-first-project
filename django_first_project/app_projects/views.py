from django.shortcuts import render
from .forms import CreateProjectForm
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
    #context = {"projects": projects_list}
    context = {"projects": my_projects}
    return render(request, "app_projects/projects.html", context)


def project(request, pk):
    selected_project = Project.objects.get(id=pk)
    context = {"project": selected_project}
    return render(request, "app_projects/project.html", context)


def create_project(request):
    form = CreateProjectForm()
    context = {"form": form}

    return render(request, "app_projects/create.html", context)
