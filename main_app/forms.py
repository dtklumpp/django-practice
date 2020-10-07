from django.forms import ModelForm
from .models import *

class Game_Form(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'players']

class Person_Form(ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'inclination')


    