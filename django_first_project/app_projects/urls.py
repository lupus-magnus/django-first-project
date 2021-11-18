from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects),
    path("project/<str:pk>", views.project),
    path("create", views.create_project),
]
