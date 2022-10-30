from django import forms
from cerita_perjalanan.models import ceritaPerjalananItem

class FormCerita(forms.ModelForm):
    class Meta:
        model = ceritaPerjalananItem
        fields = {"name", "review"}
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            # "email": forms.EmailInput(attrs={"class": "form-control"}),
            "review": forms.TextInput(attrs={"class": "form-control"})}