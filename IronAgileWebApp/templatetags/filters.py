from django import template
from IronAgileWebApp.models import *
from django.utils.translation import ugettext as _
import json
import datetime

register = template.Library()

@register.simple_tag
def getInscriptionEnCour(session, id):
    try:
        concerner = Concerner.objects.get(fk_userProfile=session, fk_evenement=id)
        if concerner:
            return True
        else:
            return False
    except:
        return False



