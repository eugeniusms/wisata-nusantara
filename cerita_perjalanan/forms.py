from django import forms
from cerita_perjalanan.models import ceritaPerjalananItems

class FormCerita(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'form-control block w-full p-4 bg-white bg-clip-padding border border-solid border gray-300 rounded-md ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none hidden',
    #     'placeholder':'Name',
    #     'value':'{{username}}'
    # }))
    review = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control block w-full p-4 text-gray bg-white bg-clip-padding border border-solid border gray transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
    }))
        
    class Meta:
        model = ceritaPerjalananItems
        fields = {"review"}
4