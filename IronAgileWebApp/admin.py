from django.contrib import admin
from IronAgileWebApp.models import *


# Register your models here.

class EvenementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Evenement)


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile)

class ConcerneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Concerner)
