
from django.shortcuts import redirect, render



def lost(request):
    return render(request, 'lostPw.html')