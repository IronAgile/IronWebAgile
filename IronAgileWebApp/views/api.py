from rest_framework import viewsets
from IronAgileWebApp.models import *
from IronAgileWebApp.serializers import *

class ConcernerViewSet(viewsets.ModelViewSet):
    user = UserSerializer()
    queryset = Concerner.objects.all()
    serializer_class = ConcernerSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer