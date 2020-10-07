from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hiya</h1>')

def games_index(request):
    games = Game.objects.all()
    context = {
        "game_list": games,
    }
    return render(request, 'games/index.html', context)
