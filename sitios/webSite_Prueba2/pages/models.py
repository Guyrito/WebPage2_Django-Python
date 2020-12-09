from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model): 
    title = models.CharField(max_length=50, verbose_name ="Titulo")
    content = RichTextField(verbose_name ="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name ="Fecha_creacion")
    update = models.DateTimeField(auto_now=True,verbose_name ="Fecha_edicion")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order']

    def __str__(self):
        return self.title