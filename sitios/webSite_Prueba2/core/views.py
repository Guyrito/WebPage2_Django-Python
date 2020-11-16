from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"core/home.html")
def ps4(request):
    return render(request,"core/ps4.html")
def steam(request):
    return render(request,"core/steam.html")
def contact(request):
    return render(request,"core/contact.html")
def aboutUs(request):
    return render(request,"core/aboutUs.html")





