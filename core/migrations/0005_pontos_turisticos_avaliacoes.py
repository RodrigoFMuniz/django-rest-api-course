# Generated by Django 3.2.12 on 2022-02-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontos_turisticos_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos_turisticos',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
