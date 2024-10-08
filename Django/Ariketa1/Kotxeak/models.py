from django.db import models
from django.utils import timezone

class Kotxe(models.Model):
    matrikula = models.CharField(max_length=75, primary_key=True)
    marka = models.CharField(max_length=100)
    modeloa = models.CharField(max_length=100)
    kolorea = models.CharField(max_length=50)
    urtea = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Matricula: {self.matrikula}, Marka: {self.marka}, Modeloa: {self.modeloa}, Kolorea: {self.kolorea}, Urtea: {self.urtea.year}"


class Pertsona(models.Model):
    Dni = models.CharField(max_length=75, primary_key=True)
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    Telefonoa = models.CharField(max_length=50)
    Jaiotze_data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Izena: {self.izena}, Abizena: {self.abizena}, DNI: {self.Dni}, Telefonoa: {self.Telefonoa}"
    
    
class Alokatu(models.Model):
    id = models.AutoField(primary_key=True)
    kotxe_id = models.ForeignKey(Kotxe, on_delete=models.CASCADE) 
    pertsona_id = models.ForeignKey(Pertsona, on_delete=models.CASCADE)
    alokairu_data = models.DateTimeField(default=timezone.now)
    itzulketa_data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Alokairua ID: {self.id}, Kotxe: {self.kotxe_id.matrikula}, Pertsona: {self.pertsona_id.izena} {self.pertsona_id.abizena}, Alokairu Data: {self.alokairu_data}, Itzulketa Data: {self.itzulketa_data}"
    

