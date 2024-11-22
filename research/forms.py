from django import forms
from .models import ResearchProject, Researcher

class ResearcherForm(forms.ModelForm):
    class Meta:
        model = Researcher
        fields = ['first_name', 'last_name', 'email', 'contacts', 'address']

class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ['title', 'description', 'start_date', 'end_date', 'researchers']
