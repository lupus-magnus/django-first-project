from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects),
    path("project/edit/<str:pk>", views.edit_project),
    path("project/delete/<str:pk>", views.delete_project),
    path("project/<str:pk>", views.project),
    path("create", views.create_project),
]
