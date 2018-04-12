from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
#from IronAgileWebApp.forms import RegisterForm

from IronAgileWebApp.models import UserProfile


def register(request):



    return render(request, 'nouveauCompteForms.html')