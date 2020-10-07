from django.forms import ModelForm
from .models import Game

class Game_Form(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'players']
