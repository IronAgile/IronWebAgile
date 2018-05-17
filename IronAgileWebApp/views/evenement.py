from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from IronAgileWebApp.models import *
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator




@login_required(login_url='login/')
def listEvenement(request):
    """Vue qui retourne la liste de tous les evenements"""

    evenement = Evenement.objects.all()

    return render(request, 'listEvenement.html', {'Evenement':evenement})

@login_required(login_url='login/')
def InscriptionEvenement(request, id):

    eve = Evenement.objects.get(pk=id)
    inscription = Concerner.objects.create(fk_evenement=eve, fk_userProfile=request.user)
    inscription.save()

    return redirect('/')

@login_required(login_url='login/')
def SupprimerInscriptionEvenement(request, id):
    eve = Evenement.objects.get(pk=id)
    inscription = Concerner.objects.filter(fk_evenement=eve, fk_userProfile=request.user).delete()
    return redirect('/')

@login_required(login_url='login/')
def mesInscriptions(request):
    inscription = Evenement.objects.filter(concerner__fk_userProfile=request.user)
    return render(request, 'mesInscriptions.html', {'inscriptions' : inscription})


@login_required(login_url='login/')
def voirDetailEvenement(request, id):
    eve = Evenement.objects.get(id=id)
    nb = Concerner.objects.filter(fk__evenement=eve).count()
    return render(request, 'voirDetailEvenement.html', {'evenement': eve, 'nb_inscrit':nb})


@login_required(login_url='login/')
def detailsEvenements(request):
    evenement = Evenement.objects.all()
    return render(request, 'listDetailEvenement.html', {'Evenement':evenement})


@login_required(login_url='login/')
def voirEvenement(request,id):
    evenement = Evenement.objects.get(id=id)
    return render(request, 'listInscritEvenement.html', {'Evenement': evenement})