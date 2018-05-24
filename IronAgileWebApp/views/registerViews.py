from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
#from IronAgileWebApp.forms import RegisterForm
from django.contrib import messages
from IronAgileWebApp.models import Profile


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from IronAgileWebApp.forms.registerForm import *

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)

        if form.is_valid():
            print('form valider !!')
            form.username = form.cleaned_data.get('email')
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('email')
            user.save()

            user = form.save()

            user.refresh_from_db()  # load the profile instance created by the signal

            user.profile.civilite = form.cleaned_data.get('civilite')
            user.profile.adresse = form.cleaned_data.get('adresse')

            user.profile.codePostal = form.cleaned_data.get('codePostal')
            user.profile.ville = form.cleaned_data.get('ville')
            user.profile.username = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')

            return redirect('login')
        else:
            messages.add_message(request, messages.INFO, form.errors)


    else:
        form = SignUpForm()
    return render(request, 'nouveauCompteForms.html', {'form': form})