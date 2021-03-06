# Generated by Django 3.2.7 on 2021-09-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portfolio')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Direccion web')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Projecto',
                'verbose_name_plural': 'Projectos',
                'ordering': ('-created',),
            },
        ),
    ]
