
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import get_template
from django.views import View
from .forms import ProjetForm, ItemForm, ArticleAdd
from .models import Projet, Chef_Projet, Article, ProjArti, Utilisateur, Responsable_Projet
import _datetime
from .utils import render_to_pdf
from .forms import tacheFrom

def home(request,pk):
    projets = Projet.objects.all()
    chefs = Chef_Projet.objects.all()
    projets_total = projets.count()
    chefs_total = chefs.count()
    responsable= Responsable_Projet.objects.get(id=pk)
    context = {'projets': projets, 'projets_total': projets_total, 'chefs_total': chefs_total,'responsable':responsable}
    return render(request, 'projet/responsable_projet/acceuil.html', context)

def ajouter_projet(request, pk):
    responsable= Responsable_Projet.objects.get(id=pk)
    form = ProjetForm()
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            ch='/Responsable/'+pk+'/liste_Projet'
            return redirect(ch)
    context = {'form': form,'responsable':responsable}
    return render(request, 'projet/responsable_projet/ajouter_projet.html', context)

def modifier_projet(request,pk,proj):
    responsable= Responsable_Projet.objects.get(id=pk)
    projet = Projet.objects.get(id=proj)
    form = ProjetForm(instance=projet)
    if request.method == 'POST':
        form = ProjetForm(request.POST,instance=projet)
        if form.is_valid():
            form.save()
            ch='/Responsable/'+pk+'/liste_Projet'
            return redirect(ch)
    context = {'form': form, projet:'projet','responsable':responsable}
    return render(request, 'projet/responsable_projet/modifier_projet.html', context)

def supprimer_projet(request,proj,pk):
    responsable= Responsable_Projet.objects.get(id=pk)
    projet = Projet.objects.get(id=proj)
    if request.method == 'POST':
        projet.delete()
        ch = '/Responsable/' +pk+ '/liste_Projet'
        return redirect(ch)
    context = {'item': projet,'responsable':responsable,'projet':projet}
    return render(request, 'projet/responsable_projet/supprimer_projet.html', context)


def listprojet(request,pk):
    responsable= Responsable_Projet.objects.get(id=pk)
    projets = Projet.objects.all()
    chefs = Chef_Projet.objects.all()
    context = {'projets': projets,'responsable':responsable,'chefs':chefs}
    return render(request, 'projet/responsable_projet/list_projet.html', context)

def listeChef(request,pk):
    responsable= Responsable_Projet.objects.get(id=pk)
    chefs = Chef_Projet.objects.all()
    context = {'chefs': chefs,'responsable':responsable}
    return render(request, 'projet/responsable_projet/list_chef.html', context)


# chef_projet


def homechef(request,pk):
    chef_projet = Chef_Projet.objects.get(id=pk)
    projet = chef_projet.projet_set.all()
    projet_total = projet.count()
    context = {'chef_projet': chef_projet, 'projet': projet, 'projet_total': projet_total}
    return render(request, 'projet/chef_projet/acceuil.html', context)

def list_projet(request,pk):
    chef_projet = Chef_Projet.objects.get(id=pk)
    projet = chef_projet.projet_set.all()
    projet_total = projet.count()
    context = {'chef_projet': chef_projet,'projet': projet, 'projet_total': projet_total}
    return render(request, 'projet/chef_projet/liste_projets.html', context)


def ajouter_article(request,pk, proj):
    articles = Article.objects.all()
    projet = Projet.objects.get(id=proj)
    chef = Chef_Projet.objects.get(id=pk)
    context = {'article': articles, 'projet': projet, 'chef_projet': chef}
    return render(request, 'projet/chef_projet/ajouter_article.html', context)


def ajouter_article2(request,pk, arti, proj):
    articles = Article.objects.get(code_article=arti)
    projet = Projet.objects.get(id=proj)
    chef = Chef_Projet.objects.get(id=pk)
    context = {'art': articles, 'projet': projet, 'chef_projet': chef}
    return render(request, 'projet/chef_projet/ajouter_article2.html', context)


def comfirmer_article(request,pk, arti, proj):
    projet = Projet.objects.get(id=proj)
    chef = Chef_Projet.objects.get(id=pk)
    articles = Article.objects.get(code_article=arti)
    num = request.POST.get('number')
    if articles.dispo_article >= int(num):
        test = True
        projarti = ProjArti()
        projarti.article = articles
        projarti.projet = Projet.objects.get(id=proj)
        projarti.chef_projet = Chef_Projet.objects.get(id=pk)
        projarti.nombre = int(num)
        projarti.date_ajout = _datetime.date.today()
        projarti.save()
        art = Article.objects.get(code_article=arti)
        art.dispo_article = art.dispo_article-int(num)
        art.save()
    else:

        test = False
    context = {'test': test ,'chef_projet':chef,'projet':projet}
    return render(request, 'projet/chef_projet/comfirmer_article.html', context)




def detaille_projet(request,pk,proj):
    projet = Projet.objects.get(id=proj)
    chef = Chef_Projet.objects.get(id=pk)
    tache = projet.tache_set.all()
    context = {'projet': projet,'chef_projet':chef,'tache':tache}
    return render(request, 'projet/chef_projet/detaille_projet.html', context)

def ajout_tache (request,pk,proj):
    form = tacheFrom()
    projet = Projet.objects.get(id=proj)
    chef = Chef_Projet.objects.get(id=pk)
    if request.method == 'POST':
        form = tacheFrom(request.POST)
        if form.is_valid():
            form.save()
            ch='/chefProjet/'+str(pk)+'/detaille_projet/'+proj
            return redirect(ch)
    context = {
        'form': form,
        'projet': projet,
        'chef_projet': chef}
    return render(request, 'projet/chef_projet/ajout_tache.html',context)

class GeneratePdf(View):
    def get(self, request, pk, **kwargs):
        template=get_template('projet/chef_projet/pdf_detail.html')
        projet = Projet.objects.get(id=pk)
        context = {'projet': projet}
        html= template.render(context)
        pdf = render_to_pdf('projet/chef_projet/pdf_detail.html',context)
        return HttpResponse(pdf,content_type='application/pdf')