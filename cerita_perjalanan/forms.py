from django import forms
from cerita_perjalanan.models import ceritaPerjalananItems

class FormCerita(forms.ModelForm):
    class Meta:
        model = ceritaPerjalananItems
        fields = {"name", "email", "review"}