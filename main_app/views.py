from django.shortcuts import render, redirect
from django.http import HttpResponse
# internal imports
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hiya</h1>')

def games_index(request):
    games = Game.objects.all()
    game_form = Game_Form()
    context = {
        "game_list": games,
        "game_form": game_form,
    }
    return render(request, 'games/index.html', context)

def games_create(request):
    if request.method == "POST":
        game_form = Game_Form(request.POST)
        if game_form.is_valid():
            game_form.save()
            return redirect('/games/')


def games_show(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {
        "game": game,
    }
    return render(request, 'games/show.html', context)

def games_edit(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == "POST":
        game_form = Game_Form(request.POST, instance=game)
        if game_form.is_valid():
            edited_form = game_form.save(commit=False)
            edited_form.save()
            return redirect('games-show', game_id=game_id)
    game_form = Game_Form(instance=game)
    context = {
        "game": game,
        "game_form": game_form,
    }
    return render(request, 'games/edit.html', context)

def games_delete(request, game_id):
    game = Game.objects.get(id=game_id)
    game.delete()
    return redirect('/games/')
