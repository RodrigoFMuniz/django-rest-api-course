# Generated by Django 3.2.12 on 2022-02-13 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_pontos_turisticos_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos_turisticos',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]