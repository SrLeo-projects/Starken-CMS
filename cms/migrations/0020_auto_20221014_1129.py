# Generated by Django 3.2.16 on 2022-10-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0019_auto_20221014_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='cuarta_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='about',
            name='primera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='about',
            name='quinta_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='about',
            name='segunda_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='about',
            name='tercera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='primera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='segunda_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='home',
            name='cuarta_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='home',
            name='primera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='home',
            name='quinta_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='home',
            name='segunda_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='home',
            name='tercera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='preguntascategoria',
            name='primera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='preguntasfrecuentes',
            name='primera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='preguntasfrecuentes',
            name='segunda_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='preguntasfrecuentes',
            name='tercera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='starkenpro',
            name='primera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='starkenpro',
            name='segunda_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
        migrations.AddField(
            model_name='starkenpro',
            name='tercera_seccion_ocultar',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
    ]