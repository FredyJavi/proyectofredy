# Generated by Django 3.2.7 on 2023-05-25 20:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_alter_contenidos_empresa_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenidos_empresa',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenidos'),
        ),
    ]
