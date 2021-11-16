from django.shortcuts import render
from django.http import HttpResponse

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

    context = {"projects": projects_list}
    return render(request, "app_projects/projects.html", context)


def project(request, pk):
    selected_project = None
    for i in projects_list:
        if str(i["id"]) == str(pk):
            selected_project = i
    context = {"project": selected_project}
    return render(request, "app_projects/project.html", context)
