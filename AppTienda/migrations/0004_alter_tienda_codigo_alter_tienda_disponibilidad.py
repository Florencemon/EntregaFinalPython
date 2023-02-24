# Generated by Django 4.1.6 on 2023-02-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0003_cliente_contacto_cotizar_preventa_suscribete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='codigo',
            field=models.IntegerField(help_text='Valor en ARS$'),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='disponibilidad',
            field=models.BooleanField(blank=True),
        ),
    ]