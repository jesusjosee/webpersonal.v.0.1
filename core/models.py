from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Mi nombre')
    description = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='about', verbose_name='Fotografía')

    class Meta:
        verbose_name = 'Sobre mi'
        verbose_name_plural = 'Sobre mi'

    def __str__(self) :
        return self.title


class Contact(models.Model):
    description = RichTextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    price_per_hour = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Informacion de contacto'
        verbose_name_plural = 'Informacion de contacto'

    def __str__(self) :
        return f'Informacion de contacto'

