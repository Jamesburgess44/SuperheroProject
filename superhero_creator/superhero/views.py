from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero
# Create your views here.


def index(request,):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'superhero/index.html', context)
