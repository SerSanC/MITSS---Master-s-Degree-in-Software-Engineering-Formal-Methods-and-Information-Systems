# Generated by Django 3.0.2 on 2020-01-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_socios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socios',
            name='edad',
            field=models.IntegerField(),
        ),
    ]