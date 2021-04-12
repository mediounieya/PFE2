
from django.forms import ModelForm
from django import forms

from .models import Reclamation

class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = '__all__'
        widgets = {
            'date_creation,date_traitement,date_solution': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
        }




"""<div class="field">
            <label class="label">Nom de projet</label>
            <div class="control">
              {% render_field form.objet class="input" class+="form-control" %}
            </div>
          </div>

           <div class="field">
            <label class="label">description de reclamation</label>
            <div>
              {% render_field form.description_reclamation|attr:'required:false' class="input" placeholder="Description de reclamation" class+="textarea" rows="3"  %}
            </div>
          </div>


            <div class="field">
            <label class="label">date de creation reclamation</label>
            <div class="control">
              {% render_field form.date_creation type="date"  class="datepicker" %}
            </div>
          </div>


            <div class="field">
            <label class="label">date de traitement</label>
            <div class="control">
              {% render_field form.date_traitement type="date"  class="datepicker" %}
            </div>
          </div>

             <div class="field">
            <label class="label">date de solution</label>
            <div class="control">
              {% render_field form.date_solution type="date"  class="datepicker" %}
            </div>
          </div>

        <div class="field">
            <label class="label">caracteristique de projet</label>
            <div class="control">
              {% render_field form.statut class="input" %}
            </div>
          </div>

        <div class="field">
            <label class="label">chef de projet</label>
            <div class="control">
              {% render_field form.utilisateur %}
            </div>
          </div>"""