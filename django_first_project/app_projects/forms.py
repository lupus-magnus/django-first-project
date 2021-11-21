from django import forms
from django.forms.widgets import Textarea
from .models import Project


class CreateProjectForm(forms.Form):
    name = forms.CharField(label="Project Name", max_length=80)
    description = forms.CharField(
        label="Description", widget=Textarea(), max_length=160
    )

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'