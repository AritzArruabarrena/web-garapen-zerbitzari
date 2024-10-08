from django.db import models
from django.utils import timezone

class Kotxe(models.Model):
    matrikula = models.CharField(max_length=75, primary_key=True)
    marka = models.CharField(max_length=100)
    modeloa = models.CharField(max_length=100)
    kolorea = models.CharField(max_length=50)
    urtea = models.DateTimeField(default=timezone.now)


class Pertsona(models.Model):
    Dni = models.CharField(max_length=75, primary_key=True)
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    Telefonoa = models.CharField(max_length=50)
    Jaiotze_data = models.DateTimeField(default=timezone.now)
    

