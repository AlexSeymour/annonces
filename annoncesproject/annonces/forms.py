from django.forms import ModelForm
from annonces.models import Annonce
from django import forms
class AnnonceForm(ModelForm):
    class Meta:
        model = Annonce
        fields = ['title', 'text']
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
        'text':forms.Textarea(attrs={'class':'form-control', 'rows':'5'})}

        labels = {
            'title': 'Titre',
            'text': 'Annonce'
        }