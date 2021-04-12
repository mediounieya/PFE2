from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
                  path('accueil_Responsable/<str:pk>', views.homechef, name='acceuil'),
                  path('Responsable/<int:pk>/ajouter_reclamation/', views.ajouter_reclamation_responsableProjet,name='ajouter_reclamation_responsable'),
                  path('Responsable/<int:pk>/list_reclamation/', views.list_reclamation_responsable, name='list_reclamation_responsable'),
                  path('Responsable/<str:pk>/supprimer_reclamation/<str:reclamations>', views.supprimer_reclamation_responsable, name='supprimer_reclamation_responsable'),
                  path('Responsable/<str:pk>/modifier_reclamation/<str:reclamations>', views.modifier_reclamation_responsable, name='modifier_reclamation_responsable'),


                  path('accueil_Chef/<int:pk>', views.homechef, name='acceuil_Chef'),
                  path('chefProjet/<int:pk>/ajouter_reclamation/', views.ajouter_reclamation, name='ajouter_reclamation'),
                  path('chefProjet/<int:pk>/list_reclamation/', views.list_reclamation_chef, name='list_reclamation_chef'),
                  path('chefProjet/<str:pk>/supprimer_reclamation/<str:reclamations>', views.supprimer_reclamation, name='supprimer_reclamation'),
                  path('chefProjet/<str:pk>/modifier_reclamation/<str:reclamations>', views.modifier_reclamation, name='modifier_reclamation'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
