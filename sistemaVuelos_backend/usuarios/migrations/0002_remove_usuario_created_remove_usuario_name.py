# Generated by Django 5.1.2 on 2024-11-01 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='created',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='name',
        ),
    ]
