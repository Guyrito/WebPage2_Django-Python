from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import Widget

tipo_genero = [("Masculino","1. Masculino"), ("Femenino","2. Femenino"),("Otro","3. Otro")]
preferences = [("RPG","RPG"), ("Shooters"," Shooters"),("Rol","Rol"),("Estrategia","Estrategia"),("MOBAS","MOBAS"),("Acción","Acción"),("Terror","Terror")]

class ContactForm(forms.Form):
    nick = forms.CharField(label="Nickname", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu nickname'}), min_length=3, max_length=100)
    edad = forms.IntegerField(label="Edad", required = True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresa tu edad','style': 'width:3ch'}), min_value=5, max_value=120)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Escribe tu email'}), min_length=5, max_length=100)
    genero = forms.ChoiceField(label="Género",required=True, choices= tipo_genero)
    preferencias = forms.ChoiceField(label="Preferencias",required=True, choices= preferences)
    comentarios = forms.CharField(label="Comentarios", required=False, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe tus comentarios', 'rows':4}),min_length= 10, max_length=300, initial='')