# Generated by Django 3.2.12 on 2022-02-28 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('core', '0006_pontos_turisticos_localizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontos_turisticos',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
        ),
    ]
