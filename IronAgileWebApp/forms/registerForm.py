from django import forms
from IronAgileWebApp.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from IronAgileWebApp.models import *

class SignUpForm(UserCreationForm):
    CIVILITE_CHOICES = (
        ('Mme', 'Madame',),
        ('M', 'Monsieur',),
    )
    societe = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"Société"}))
    civilite = forms.ChoiceField(choices=CIVILITE_CHOICES, widget=forms.Select(attrs={'class':"form-control", 'type':"text", 'placeholder':"Civilité"}))
    adresse = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"Adresse"}))
    codePostal = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"Code Postal"}))
    ville = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"Ville"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'type':"text", 'placeholder':"Prénom"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'type': "text", 'placeholder': "Nom"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': "form-control", 'type': "text", 'placeholder': "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'type': "password", 'placeholder': "Mot de passe"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'type': "password", 'placeholder': "Confirmer votre mot de passe"}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'societe', 'password1', 'password2', 'civilite', 'adresse', 'codePostal', 'ville', 'email', )