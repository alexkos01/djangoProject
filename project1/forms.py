from django import forms
from .models import ModelReg


class RegForm(forms.ModelForm):
    class Meta:
        model = ModelReg
        fields = ('login', 'password', 'email', 'img')