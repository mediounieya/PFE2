from django.db import models

# Create your models here.
from GestionProjet.custom_validators import validate_interval

class Utilisateur (models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    age = models.IntegerField()
    date_naiss = models.DateField()
    adresse = models.CharField(max_length=800, null=True)
    email = models.CharField(max_length=800, null=True)
    telephone = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nom
class Responsable_Projet (Utilisateur):
    def __str__(self):
        return self.nom


class Chef_Projet (Utilisateur):
    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reversed("", kwargs={"ch": self.id})


class Projet (models.Model):
    ETAT = (('a faire', 'a faire'),
              ('en cours', 'en cours'),
              ('terminé', 'terminé'))
    nom_projet = models.CharField(max_length=100, null=True)
    description_projet = models.TextField()
    adresse_projet = models.CharField(max_length=200, null=True)
    date_ajout_projet = models.DateTimeField(auto_now_add=True, null=True)
    cout_projet=models.FloatField(null=True, validators=[validate_interval])
    delai_projet = models.PositiveIntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    etat_projet = models.CharField(max_length=200, null=True, choices=ETAT)
    caracteristique_projet = models.TextField()
    chef_projet = models.ForeignKey(Chef_Projet, null=True, on_delete=models.SET_NULL)

    # Create / Insert / Add - POST
    # Retrieve / Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE

    def __str__(self):
        return self.nom_projet

class Tache(models.Model):
    titre_tache = models.CharField(max_length=200, null=False)
    description_tache = models.TextField(null=False, blank=False)
    mots_clés = models.TextField(null=True, blank=True)
    demarche_tache = models.TextField(null=True, blank=True)
    difficulté_tache = models.TextField(null=True, blank=True)
    projet = models.ForeignKey(Projet, null=True, on_delete=models.SET_NULL)



class Article (models.Model):
    code_article = models.CharField(max_length=100, null=True)
    nom_article = models.CharField(max_length=100, null=True)
    image = models.FileField(upload_to='image',blank=True)
    desc_article = models.TextField()
    dispo_article = models.IntegerField()
    categorie = models.CharField(max_length=100, null=True)


class ProjArti(models.Model):
    projet = models.ForeignKey(Projet, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)
    chef_projet = models.ForeignKey(Chef_Projet, null=True, on_delete=models.SET_NULL)
    nombre = models.IntegerField(default=0)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)
