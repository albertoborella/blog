# Generated by Django 4.1 on 2023-01-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
    ]
