from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import qrcode
from django.urls import reverse
from io import StringIO


from django.db import models

from django.core.files.uploadedfile import InMemoryUploadedFile



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

    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name

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

    def __str__(self):
        return self.titre +' le ' + self.date



    class Meta:
        unique_together = (('titre', 'date'),)


class Concerner(models.Model):
    """
        Class connaître si l'utilisateur est concerné par un événement
    """

    fk_userProfile = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    fk_evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=False)
    is_present = models.BooleanField(default=False)

    qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('events.views.details', args=[str(self.id)])

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data(self.get_absolute_url())
        qr.make(fit=True)

        img = qr.make_image()

        buffer = StringIO.StringIO()
        img.save(buffer)
        filename = 'events-%s.png' % (self.id)
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.len, None)
        self.qrcode.save(filename, filebuffer)

    class Meta:
        unique_together = (('fk_userProfile', 'fk_evenement'),)


