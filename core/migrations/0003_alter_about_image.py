# Generated by Django 3.2.7 on 2022-01-03 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220102_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about', verbose_name='Fotografía'),
        ),
    ]