from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def ps4(request):
    juegos = Project.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(juegos,2)

    try:
        juegos = paginator.page(page)
    except PageNotAnInteger:
        juegos = paginator.page(1)
    except EmptyPage:
        juegos = paginator.page(paginator.num_pages)
    return render(request, "games/ps4.html",{'juegos':juegos})
def steam(request):
    juegos = Project.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(juegos,2)
    try:
        juegos = paginator.page(page)
    except PageNotAnInteger:
        juegos = paginator.page(1)
    except EmptyPage:
        juegos = paginator.page(paginator.num_pages)
    return render(request, "games/steam.html",{'juegos':juegos})