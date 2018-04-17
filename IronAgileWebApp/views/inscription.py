from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from IronAgileWebApp.models import *
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator


def voirMesInscriptions(request):
    user_courant = User.objects.get(id=request.user)
    evenement = Evenement.objects.get(fk_evenement__concerner__fk_userProfile=user_courant)
    return render(request, 'mesInscriptions.html', {'Inscriptions' : evenement,})