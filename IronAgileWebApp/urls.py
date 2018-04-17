from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url, include

from IronAgileWebApp.views import loginViews, registerViews, lostPwViews

urlpatterns = [

    # Gestion de la session
    url('login/', loginViews.user_login),
    url('logout/', loginViews.logout_user, name='logout_user'),
    url('register/', registerViews.register, name='register'),
    url('lostpw', lostPwViews.lost, name='lostpw'),

    # Base de l'ihm accessible pour tests
    url('base', lostPwViews.base, name='base')


    ]
