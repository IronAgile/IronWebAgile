from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url, include

from IronAgileWebApp.views import loginViews, registerViews, lostPwViews, evenement, generateInvitation

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from IronAgileWebApp.views.api import *

router = routers.DefaultRouter()
router.register(r'concerner/', ConcernerViewSet)
router.register(r'evenement/', EvenementViewSet)
router.register(r'user/', UserViewSet)




urlpatterns = [

    # Gestion de la session
    path('login/', loginViews.user_login, name='login'),
    path('logout/', loginViews.logout_user, name='logout_user'),
    path('register/', registerViews.signup, name='signup'),
    path('lostpw', lostPwViews.lost, name='lostpw'),

    # Base de l'ihm accessible pour tests
    path('base', lostPwViews.base, name='base'),
    path('', evenement.listEvenement, name='index'),

    #evenement
    path('evenement/', evenement.listEvenement, name='listEvenement'),
    path('inscription/<id>/', evenement.InscriptionEvenement, name='inscriptionEvenement'),
    path('desinscrire/<id>/', evenement.SupprimerInscriptionEvenement, name='DesinscrireEvenement'),
    path('mesinscriptions/', evenement.mesInscriptions, name='mesInscriptions'),

    #generer invitation
    path('invitation/<id>/', generateInvitation.generate_invitation, name='invitation'),


    #api
    url(r'^api/', include(router.urls)),


    ]
