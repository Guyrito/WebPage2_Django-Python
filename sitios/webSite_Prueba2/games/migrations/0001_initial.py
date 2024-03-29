# Generated by Django 2.2.16 on 2020-11-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('short_description', models.TextField(verbose_name='Descripcion_corta')),
                ('image', models.ImageField(upload_to='Projects', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha_creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha_edicion')),
                ('long_description', models.TextField(verbose_name='Descripcion_larga')),
                ('precio', models.CharField(max_length=50, verbose_name='Precio')),
                ('precio_oferta', models.CharField(max_length=50, verbose_name='Precio_oferta')),
            ],
            options={
                'verbose_name': 'Juego',
                'verbose_name_plural': 'Juegos',
                'ordering': ['-created'],
            },
        ),
    ]
