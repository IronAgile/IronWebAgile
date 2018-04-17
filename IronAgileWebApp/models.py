from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    """
    Class pour la gestion des utilateurs
    """

    CIVILITE_CHOICES = (
        ('Mme', 'Madame',),
        ('M', 'Monsieur',),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    civilite = models.CharField(max_length=3, choices=CIVILITE_CHOICES)
    adresse = models.CharField(max_length=50)
    codePostal = models.CharField(max_length=5)
    ville = models.CharField(max_length=50)


class Evenement(models.Model):
    """
    Class pour la gestion des evenements
    """

    titre = models.CharField(max_length=50)
    date = models.DateField()
    heure = models.TimeField()
    adresse = models.CharField(max_length=50)
    codePostal = models.CharField(max_length=5)
    ville = models.CharField(max_length=50)

    class Meta:
        unique_together = (('titre', 'date'),)


class Concerner(models.Model):
    """
        Class connaître si l'utilisateur est concerné par un événement
    """

    fk_userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    fk_evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = (('fk_userProfile', 'fk_evenement'),)
