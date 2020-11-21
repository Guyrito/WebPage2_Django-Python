from django.shortcuts import render
from .models import Project

# Create your views here.
def ps4(request):
    juegos = Project.objects.all()
    return render(request, "games/ps4.html",{'juegos':juegos})
def steam(request):
    juegos = Project.objects.all()
    return render(request, "games/steam.html",{'juegos':juegos})