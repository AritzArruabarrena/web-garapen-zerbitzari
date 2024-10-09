from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def alokatu_list(request):
    alokatuZerrenda=Alokatu.objects.all()
    return render(request,'alokatu/alokatu_list.html' , {'alokatu':alokatuZerrenda})
