from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blouses
from .forms import Blousesform

# Create your views here.

def home(request):
    return render(request, "index.html")

def new(request):
    return HttpResponse("Explore many collections")

def blouses_view(request):
    post = Blouses.objects.all()
    return render(request, "Blouses.html", {'post': post})

def toadd(request):
    if request.method == "POST":
        form = Blousesform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a relevant page after saving
    else:
        form = Blousesform()
    
    return render(request, "toadd.html", {'form': form})


