# Generated by Django 3.0.2 on 2020-01-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200106_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquileres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_de_recogida', models.DateField(max_length=25)),
                ('fecha_de_devolucion', models.DateField(max_length=25)),
                ('total_a_pagar', models.FloatField()),
            ],
        ),
    ]
