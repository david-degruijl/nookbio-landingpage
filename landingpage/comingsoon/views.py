from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings

def coming_soon(request):
    print(settings.TEMPLATES)
    return render(request, 'comingsoon.html')
