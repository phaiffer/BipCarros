from django import forms
from .models import Argo

class ArgoForm(forms.ModelForm):
    class Meta:
        model = Argo
        fields = ['nome','descricao']