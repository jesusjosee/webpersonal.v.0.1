# Generated by Django 3.2.7 on 2022-01-03 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220102_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='user',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]