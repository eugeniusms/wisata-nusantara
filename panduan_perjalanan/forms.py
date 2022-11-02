from django import forms
from panduan_perjalanan.models import TujuanPerjalanan

class FormPerjalanan(forms.ModelForm):
  class Meta:
    model = TujuanPerjalanan
    exclude = ["user", "date"]