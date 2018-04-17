
from rest_framework import serializers
from IronAgileWebApp.models import *

class ConcernerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concerner
        fields = ('__all__')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

