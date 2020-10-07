from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
from .forms import *

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hiya</h1>')

def games_index(request):
    games = Game.objects.all()
    context = {
        "game_list": games,
    }
    return render(request, 'games/index.html', context)

def games_show(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {
        "game": game,
    }
    return render(request, 'games/show.html', context)

def games_edit(request, game_id):
    game = Game.objects.get(id=game_id)
    game_form = Game_Form()
    context = {
        "game": game,
        "game_form": game_form,
    }
    return render(request, 'games/edit.html', context)

