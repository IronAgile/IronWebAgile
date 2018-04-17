from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from IronAgileWebApp.models import *
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator


login_required(login_url='login/')

@login_required(login_url='login/')
def listEvenement(request):
    """Vue qui retourne la liste de tous les evenements"""

    evenement = Evenement.objects.all()

    return render(request, 'listEvenement.html', {'Evenement':evenement})

@login_required(login_url='login/')
def voirEvenement(request, id):
    evenement = Evenement.objects.get(id=id)
    return  render (request, 'voirEvenement.html', {'Evenement':evenement})