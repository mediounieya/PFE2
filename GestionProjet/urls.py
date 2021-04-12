from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path('accueil_Responsable/<str:pk>', views.home, name='acceuil'),
    path('Responsable/<str:pk>/listeChef', views.listeChef, name='chefs'),
    path('Responsable/<str:pk>/liste_Projet', views.listprojet, name='liste_Projet'),
    path('Responsable/<str:pk>/ajout_projet/', views.ajouter_projet, name='ajout_projet'),
    path('Responsable/<str:pk>/modifier_projet/<proj>', views.modifier_projet, name='modifier_projet'),
    path('Responsable/<str:pk>/supprimer_projet/<proj>', views.supprimer_projet, name='supprimer_projet'),

    path('accueil_Chef/<int:pk>', views.homechef, name='acceuil_Chef'),
    path('chefProjet/<int:pk>/detaille_projet/<int:proj>', views.detaille_projet, name='detaille_projet'),
    path('chefProjet/<int:pk>/ajout_tache/<proj>', views.ajout_tache, name='ajout_tache'),
    path('chefProjet/<int:pk>', views.list_projet, name='chef_projet'),
    path('chefProjet/<int:pk>/addarticle/<proj>',views.ajouter_article, name='ajouter_article'),
    path('chefProjet/<int:pk>/addarticle2/<proj>/<arti>',views.ajouter_article2, name='ajouter_article2'),
    path('chefProjet/<int:pk>/comfirmer_article/<proj>/<arti>',views.comfirmer_article, name='comfirmer_article'),
    path('pdf/<str:pk>', views.GeneratePdf.as_view(), name='pdf'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)