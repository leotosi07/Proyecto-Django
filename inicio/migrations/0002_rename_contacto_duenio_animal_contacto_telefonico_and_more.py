# Generated by Django 4.2 on 2023-04-11 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='contacto_duenio',
            new_name='contacto_telefonico',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='duenio',
            new_name='propietario',
        ),
    ]
