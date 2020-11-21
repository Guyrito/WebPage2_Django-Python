from django.db import models


# Create your models here.
class Project(models.Model): 
    title = models.CharField(max_length=50, verbose_name ="Titulo")
    short_description = models.TextField(verbose_name ="Descripcion_corta")
    image = models.ImageField(verbose_name ="Imagen", upload_to="Projects")
    created = models.DateTimeField(auto_now_add=True,verbose_name ="Fecha_creacion")
    update = models.DateTimeField(auto_now=True,verbose_name ="Fecha_edicion")
    long_description = models.TextField(verbose_name ="Descripcion_larga")
    precio = models.CharField(max_length=50, verbose_name ="Precio")
    precio_oferta = models.CharField(max_length=50, verbose_name ="Precio_oferta")

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ['-created']

    def __str__(self):
        return self.title
