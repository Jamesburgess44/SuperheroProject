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


def detail(request, superhero_id):
    specific_hero = Superhero.objects.get(pk=superhero_id)
    context = {
        'specific_hero': specific_hero
    }
    return render(request, 'superhero/detail.html', context)
