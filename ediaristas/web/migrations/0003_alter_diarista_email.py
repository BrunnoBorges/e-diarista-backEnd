# Generated by Django 3.2 on 2021-06-15 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_diarista_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarista',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
