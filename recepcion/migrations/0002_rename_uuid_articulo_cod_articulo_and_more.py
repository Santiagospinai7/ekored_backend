# Generated by Django 5.0.1 on 2024-01-25 23:28

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='uuid',
            new_name='cod_articulo',
        ),
        migrations.RenameField(
            model_name='localizacion',
            old_name='uuid',
            new_name='id_localizacion',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='uuid',
            new_name='id_ticket',
        ),
        migrations.CreateModel(
            name='ConfiguracionBascula',
            fields=[
                ('id_bascula', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('dispositivo', models.CharField(max_length=50)),
                ('tipo_pesaje', models.CharField(max_length=15)),
                ('puerto', models.IntegerField()),
                ('baudios', models.IntegerField()),
                ('paridad', models.CharField(max_length=1)),
                ('bit_de_dato', models.IntegerField()),
                ('bit_de_parada', models.IntegerField()),
                ('cadena_car_1', models.CharField(max_length=15)),
                ('cadena_car_2', models.CharField(max_length=15)),
                ('cadena_car_3', models.CharField(max_length=15)),
                ('tipo_indicador', models.CharField(max_length=20)),
                ('tipo_bascula', models.CharField(max_length=20)),
                ('ip_dispositivo', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=150)),
                ('peso_patron', models.FloatField()),
                ('tolerancia', models.FloatField()),
                ('pesaje_automatico', models.BooleanField()),
                ('id_acopio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.acopio')),
            ],
            options={
                'db_table': '[bascula].[tblEKOConfiguracionBasculas]',
            },
        ),
    ]