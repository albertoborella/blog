# Generated by Django 4.1 on 2023-01-03 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0002_alter_post_publicado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contenido',
        ),
    ]
