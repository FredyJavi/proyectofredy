# Generated by Django 3.2.7 on 2023-05-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0010_project_link_red'),
    ]

    operations = [
        migrations.CreateModel(
            name='redes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Direccion Web')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='link_red',
        ),
    ]
