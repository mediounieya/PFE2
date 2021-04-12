from django.contrib import admin

# Register your models here.
from GestionProjet.models import Chef_Projet, Projet, Article, ProjArti, Tache, Responsable_Projet, Utilisateur

admin.site.register(Chef_Projet)
admin.site.register(Responsable_Projet)
admin.site.register(Utilisateur)
admin.site.register(Projet)
admin.site.register(Article)
admin.site.register(ProjArti)
admin.site.register(Tache)