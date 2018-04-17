from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
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


    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

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

    fk_userProfile = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    fk_evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=False)
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = (('fk_userProfile', 'fk_evenement'),)
