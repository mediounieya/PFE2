from django.forms import ModelForm
from django import forms

from .models import Projet, Article, Tache


def is_past_due(date_debut,date_fin):
    return date_fin > date_debut
class ProjetForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields='__all__'
        widgets = {
            'date_debut,date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
        }
        date_debut = forms.DateField()
    def clean(self):
        cleaned_data = super().clean()
        forms.date_debut = cleaned_data.get('date_debut')
        forms.date_fin = cleaned_data.get('date_fin')

        if forms.date_debut and forms.date_fin:
            if not is_past_due(forms.date_debut,forms.date_fin):
                 raise forms.ValidationError('date fin est superieur a date debut !!')


class ItemForm(ModelForm):
    class Meta:
        model = Projet
        fields =['chef_projet']

class ArticleAdd(forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'

class tacheFrom(ModelForm):
    class Meta:
        model = Tache
        fields = '__all__'
