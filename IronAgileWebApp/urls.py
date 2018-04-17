from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url, include

from IronAgileWebApp.views import loginViews, registerViews, lostPwViews, evenement

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from IronAgileWebApp.views.api import *

router = routers.DefaultRouter()
router.register(r'concerner', ConcernerViewSet)
router.register(r'user/', UserViewSet)




urlpatterns = [

    # Gestion de la session
    url('login/', loginViews.user_login, name='login'),
    url('logout/', loginViews.logout_user, name='logout_user'),
    url('register/', registerViews.signup, name='signup'),
    url('lostpw', lostPwViews.lost, name='lostpw'),

    # Base de l'ihm accessible pour tests
    url('base', lostPwViews.base, name='base'),
    url('', evenement.listEvenement, name='index'),

    #evenement
    url('evenement', evenement.listEvenement, name='listEvenement'),
    url('evenement/<id>/', evenement.voirEvenement, name='voirEvenement'),

    #api
    url(r'^api/', include(router.urls)),


    ]
