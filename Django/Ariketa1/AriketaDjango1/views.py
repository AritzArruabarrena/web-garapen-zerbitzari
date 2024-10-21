from django.shortcuts import render , redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
# Create your views here.
def ikasle_list(request):
    ikasleZerrenda=Ikasle.objects.all()
    return render(request, 'zerrenda/ikasle_list.html',{'ikasleak':ikasleZerrenda})

def notak_list(request):
    notakZerrenda=Notak.objects.all()
    return render(request, 'zerrenda/notak_list.html',{'notak':notakZerrenda})

def ikasle_new(request):
    if request.method == 'POST':
        form = IkasleForm(request.POST)
        if form.is_valid():  # <- Add parentheses
            ikasle = form.save()
            return redirect('default')  # <- Redirect after saving

    else:
        form = IkasleForm()
    
    return render(request, 'zerrenda/ikasleform.html', {'form': form})

    

def ikasgai_new(request):
    if request.method == 'POST':
        form=IkasgaiakForm(request.POST)
        if form.is_valid:
            ikasgaiak = form.save()
            ikasgaiak.save()
        return redirect('default')

    else:
        form=IkasgaiakForm()
        return render(request, 'zerrenda/ikasgaiaform.html', {'form':form})


def notak_new(request):
    if request.method == 'POST':
        form=NotakForm(request.POST)
        if form.is_valid:
            notak = form.save()
            notak.save()
        return redirect('default')

    else:
        form=NotakForm()
        return render(request, 'zerrenda/notakform.html', {'form':form})
    


def notakEditatu_new(request, ikasle_id, ikasgai_id):
    notak = Notak.objects.filter(ikasle_id=ikasle_id, ikasgai_id=ikasgai_id)
    
    notakeditatu = notak.first()
    
    if not notakeditatu:
        return render(request, 'error.html', {'message': 'No se encontró la nota'})

    if request.method == 'POST':
        form = NotakEditatuForm(request.POST, instance=notakeditatu)
        if form.is_valid():
            form.save()
            return redirect('default')  
    else:
        form = NotakEditatuForm(instance=notakeditatu)

    return render(request, 'zerrenda/notakform.html', {'form': form})

def ikasleaEzabatu(request, ikasle_id):
    ikaslea = Ikasle.objects.filter(id=ikasle_id) 
    
    ikaslea.delete()  
    return redirect('default')

def logout_view(request):
    logout(request)
    return redirect("default")


    

         
