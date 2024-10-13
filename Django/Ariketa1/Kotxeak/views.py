from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def alokatu_list(request):
    alokatuZerrenda=Alokatu.objects.all()
    return render(request,'alokatu/alokatu_list.html' , {'alokatu':alokatuZerrenda})

def kotxeko_datuak(request):
    return render(request, 'kotxeak/kotxeak.html')

def kotxeko_datuak_ikusi(request):
    return render(request, 'kotxeak/kotxeko-datuak.html')

def kotxeko_datuak_list(request):
    kotxeZerrenda = Kotxe.objects.all()
    return render(request, 'kotxeak/kotxeak_list.html', {'kotxe': kotxeZerrenda})


def pertsona_datuak(request):
    return render(request, 'pertsonak/pertsona.html')


