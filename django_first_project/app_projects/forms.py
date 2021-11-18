from django import forms
from django.forms.widgets import Textarea


class CreateProjectForm(forms.Form):
    name = forms.CharField(label="Project Name", max_length=80)
    description = forms.CharField(
        label="Description", widget=Textarea(), max_length=160
    )
