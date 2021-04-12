from django.shortcuts import render, redirect

# Create your views here.
from GestionProjet.models import Chef_Projet, Responsable_Projet, Projet, Utilisateur
from GestionReclamation.forms import ReclamationForm
from GestionReclamation.models import Reclamation

#chef_projet
def ajouter_reclamation(request,pk):
    chef_projet = Chef_Projet.objects.get(id=pk)
    form = ReclamationForm()
    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            form.save()
            ch = '/chefProjet/' + pk + '/list_reclamation'
            return redirect(ch)
    context = {'form': form,'chef_projet':chef_projet}
    return render(request, 'projet/chef_projet/ajouter_reclamation.html', context)

def list_reclamation_chef(request,pk):
    chef_projet = Utilisateur.objects.get(id=pk)
    reclamations = chef_projet.reclamation_set.all()
    context = {'chef_projet': chef_projet, 'reclamations': reclamations}
    return render(request, 'projet/chef_projet/list_reclamation.html', context)



def supprimer_reclamation(request,reclamations,pk):
    chef_projet= Utilisateur.objects.get(id=pk)
    reclamations = Reclamation.objects.get(id=reclamations)
    if request.method == 'POST':
        reclamations.delete()
        ch = '/chefProjet/' +pk+ '/list_reclamation'
        return redirect(ch)
    context = {'item': reclamations,'chef_projet':chef_projet,'reclamations':reclamations}
    return render(request, 'projet/chef_projet/supprimer_reclamation.html', context)


def modifier_reclamation(request, reclamations, pk):
    chef_projet = Utilisateur.objects.get(id=pk)
    reclamations = Reclamation.objects.get(id=reclamations)
    form= ReclamationForm(instance=reclamations)
    if request.method == 'POST':
        form = ReclamationForm(request.POST,instance=reclamations)
        if form.is_valid():
            form.save()
            ch = '/chefProjet/' + pk + '/list_reclamation'
            return redirect(ch)
    context = {'form': form,'chef_projet':chef_projet,'reclamations':reclamations}
    return render(request, 'projet/chef_projet/modifier_reclamation.html', context)


def homechef(request,pk):
    chef_projet = Chef_Projet.objects.get(id=pk)
    projet = chef_projet.projet_set.all()
    projet_total = projet.count()
    context = {'chef_projet': chef_projet, 'projet': projet, 'projet_total': projet_total}
    return render(request, 'projet/chef_projet/acceuil.html', context)




  # responsable projet

def home(request,pk):
    projets = Projet.objects.all()
    chefs = Chef_Projet.objects.all()
    projets_total = projets.count()
    chefs_total = chefs.count()
    responsable= Responsable_Projet.objects.get(id=pk)
    context = {'projets': projets, 'projets_total': projets_total, 'chefs_total': chefs_total,'responsable':responsable}
    return render(request, 'projet/responsable_projet/acceuil.html', context)
def list_reclamation_responsable(request,pk):
    responsable = Responsable_Projet.objects.get(id=pk)
    reclamations = responsable.reclamation_set.all()
    context = {'responsable': responsable, 'reclamations': reclamations}
    return render(request,'projet/responsable_projet/list_reclamation.html', context)

def ajouter_reclamation_responsableProjet(request,pk):
    responsable = Responsable_Projet.objects.get(id=pk)
    form = ReclamationForm()
    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            form.save()
            ch= '/accueil_Responsable/'+str(pk)
            return redirect(ch)
    context = {'form': form,'responsable':responsable}
    return render(request, 'projet/responsable_projet/ajouter_reclamation.html', context)


def supprimer_reclamation_responsable(request,reclamations,pk):
    responsable= Responsable_Projet.objects.get(id=pk)
    reclamations = Reclamation.objects.get(id=reclamations)
    if request.method == 'POST':
        reclamations.delete()
        ch = '/Responsable/' +pk+ '/list_reclamation'
        return redirect(ch)
    context = {'item': reclamations,'responsable':responsable,'reclamations':reclamations}
    return render(request, 'projet/responsable_projet/supprimer_reclamation.html', context)


def modifier_reclamation_responsable(request, reclamations, pk):
    responsable = Responsable_Projet.objects.get(id=pk)
    reclamations = Reclamation.objects.get(id=reclamations)
    form= ReclamationForm(instance=reclamations)
    if request.method == 'POST':
        form = ReclamationForm(request.POST,instance=reclamations)
        if form.is_valid():
            form.save()
            ch = '/Responsable/' + pk + '/list_reclamation'
            return redirect(ch)
    context = {'form': form,'responsable':responsable,'reclamations':reclamations}
    return render(request, 'projet/responsable_projet/modifier_reclamation.html', context)