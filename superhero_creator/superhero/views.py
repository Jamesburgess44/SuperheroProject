from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse
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


def delete(request, superhero_id):
    superhero_delete = Superhero.objects.get(pk=superhero_id)
    superhero_delete.delete()
    context = {
        'superhero_delete': superhero_delete
    }
    return HttpResponseRedirect(reverse(request, 'specific_hero.id', context))


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego_name')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_superhero = Superhero(name=name, alter_ego_name=alter_ego_name,
                                  primary_superhero_ability=primary_superhero_ability,
                                  secondary_superhero_ability=secondary_superhero_ability,
                                  catch_phrase=catch_phrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superhero:index'))
    else:
        return render(request, 'superhero/create.html')


def edit(request, superhero_id):
    superhero_edit = Superhero.objects.get(pk=superhero_id)
    context = {
            'superhero_edit': superhero_edit
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego_name = request.POST.get('alter_ego')
        primary_superhero_ability = request.POST.get('primary_superhero_ability')
        secondary_superhero_ability = request.POST.get('secondary_superhero_ability')
        catch_phrase = request.POST.get('catchphrase')
        superhero_edit = Superhero(name=name,
                                alter_ego_name=alter_ego_name,
                                primary_superhero_ability=primary_superhero_ability,
                                secondary_superhero_ability=secondary_superhero_ability,
                                catch_phrase=catch_phrase)
        superhero_edit.save(superhero_id)
        return HttpResponseRedirect(reverse('superhero:index'))
    else:
        return render(request, "superhero/edit.html", context)