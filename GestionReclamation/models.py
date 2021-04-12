from GestionProjet import models
from django.db import models

# Create your models here.
from GestionProjet.models import Utilisateur


class Reclamation(models.Model):
    objet = models.CharField(max_length=200, null=False)
    description_reclamation = models.TextField(null=False, blank=False)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    date_traitement = models.DateField(null=False)
    date_solution = models.DateField(null=False)
    statut = models.CharField(max_length=200, null=False)
    utilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.objet