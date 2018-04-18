
from django.shortcuts import redirect, render



def lost(request):
    return render(request, 'lostPw.html')

def base(request):
    return render(request, 'base.html')