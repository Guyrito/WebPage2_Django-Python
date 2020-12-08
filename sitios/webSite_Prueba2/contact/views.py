from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    #print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            nick = request.POST.get('nick','')
            edad = request.POST.get('edad','')
            email = request.POST.get('email','')
            genero = request.POST.get('genero','')
            preferencias = request.POST.get('preferencias','')
            comentarios = request.POST.get('comentarios','')
            
            #Crear el correo que se enviará
            email = EmailMessage(
                "Gamestore: Un nuevo mensaje ha llegado D:",
                "De {} <{}>\n\nEscribió:\n\n{}\n\nSus datos son:\nEdad: {}\nGénero: {}\nPreferencias: {}".format(nick,email,comentarios,edad,genero,preferencias),
                "no-contestar@inbox.mailtrap.io",
                ["dieg.ortegav@alumnos.duoc.cl"],
                reply_to = [email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + "?OK")
            except:
                return redirect(reverse('contact') + "?FAIL")
        

    return render(request,"contact/contact.html", {'form':contact_form})