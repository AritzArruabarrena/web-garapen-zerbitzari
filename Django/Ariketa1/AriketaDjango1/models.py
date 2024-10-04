from django.db import models
from django.utils import timezone

class Ikasle(models.Model):
 id = models.AutoField(primary_key=True)
 izena = models.CharField(max_length=75)
 abizena = models.CharField(max_length=100)
 jaiotze_data = models.DateTimeField(default=timezone.now)
 def __str__(self):
    return f"Ikaslearen izena {self.izena} da eta abizenak {self.abizena}."

class Ikasgaiak(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    maila = models.CharField(max_length=100)
    hizkuntza = models.CharField(max_length=75)
    
    def __str__(self):
        return f"Ikasgaiaren izena: {self.izena}, maila: {self.maila}, hizkuntza: {self.hizkuntza}."

class Notak(models.Model):
    nota = models.DecimalField(max_digits=5,decimal_places=2)
    oharra = models.CharField(max_length=75)
    ikasgai = models.ForeignKey(Ikasgaiak, on_delete=models.CASCADE) 
    ikasle = models.ForeignKey(Ikasle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Ikasle: {self.ikasle.izena} {self.ikasle.abizena} - Ikasgai: {self.ikasgai.izena} - Nota: {self.nota}"