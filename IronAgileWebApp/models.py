from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Class pour la gestion des utilateurs
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=50)
    codePostal = models.CharField(max_length=5)
    ville = models.CharField(max_length=50)


