from django import forms
from notes.models import Notes
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = "__all__"
