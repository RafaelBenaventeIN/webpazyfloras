# Generated by Django 4.1.3 on 2022-12-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_pedidoservicio_terminos_acordados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoservicio',
            name='duracion',
        ),
        migrations.AddField(
            model_name='pedidoservicio',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
