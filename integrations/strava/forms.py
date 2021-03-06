from django.forms import ModelForm
from project.models import Project

class StravaForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'secret', 'client_id', 'callbackUrl', 'scope', 'state']
