from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    inclination = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    players = models.IntegerField()

    people = models.ManyToManyField(Person)

    def __str__(self):
        return self.name

