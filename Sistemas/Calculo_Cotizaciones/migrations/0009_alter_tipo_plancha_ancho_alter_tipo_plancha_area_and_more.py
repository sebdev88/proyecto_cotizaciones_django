# Generated by Django 4.2.5 on 2023-11-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculo_Cotizaciones', '0008_alter_tipo_plancha_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_plancha',
            name='ancho',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tipo_plancha',
            name='area',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tipo_plancha',
            name='largo',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
