from django.shortcuts import render , redirect
from django.contrib.auth import logout

def home(request):
    return render(request , "base.html")

def logout_view(request):
    logout(request)
    return redirect("/")