# Generated by Django 4.0.4 on 2022-06-08 19:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_alter_publicacion_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='descripcion',
            field=tinymce.models.HTMLField(blank=True, max_length=280, null=True, verbose_name='Descripcion'),
        ),
    ]
