# Generated by Django 3.2.7 on 2023-05-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0002_delete_contenidos_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='contenidos_empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('contenido_mision', models.TextField(verbose_name='Contenido_Mision')),
                ('contenido_vision', models.TextField(verbose_name='Contenido_Vision')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')),
            ],
            options={
                'verbose_name': 'Contenido',
                'verbose_name_plural': 'Contenidos',
            },
        ),
    ]