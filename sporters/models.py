from django.db import models

# Create your models here.

class speler(models.Model):
    naam = models.CharField(max_length=25)
    voornaam = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, default= "test@gmail.com")

class match_punten(models.Model):
    nummerSpeler = models.IntegerField()
    punten = models.IntegerField()
    matchCode = models.IntegerField()