# Generated by Django 3.2 on 2021-06-16 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_rename_telefone_diarista_telefon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diarista',
            old_name='telefon',
            new_name='telefone',
        ),
    ]
