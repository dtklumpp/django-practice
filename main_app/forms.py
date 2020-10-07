from django.forms import ModelForms
from .models import Game

class Game_Form(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'players']
