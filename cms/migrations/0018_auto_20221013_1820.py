# Generated by Django 3.2.16 on 2022-10-13 23:20

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_sucursales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('primera_seccion_titulo_imagen', models.CharField(blank=True, max_length=255, null=True, verbose_name='título imagen')),
                ('primera_seccion_alt_imagen', models.CharField(blank=True, max_length=255, null=True, verbose_name='alt imagen')),
                ('primera_seccion_imagen', models.ImageField(blank=True, null=True, upload_to='seguimiento', verbose_name='imagen miniatura')),
                ('primera_seccion_video_url', models.URLField(blank=True, null=True, verbose_name='url del video')),
                ('primera_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('primera_seccion_descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('primera_seccion_boton', models.CharField(blank=True, max_length=255, null=True, verbose_name='botón')),
                ('primera_seccion_boton_url', models.URLField(blank=True, null=True, verbose_name='url del botón')),
            ],
            options={
                'verbose_name': 'Covid-19',
                'verbose_name_plural': 'Covid-19',
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='primera_seccion_fecha',
            field=models.DateField(blank=True, null=True, verbose_name='fecha'),
        ),
        migrations.CreateModel(
            name='CovidComunicado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primera_seccion_fecha', models.DateField(blank=True, null=True, verbose_name='fecha')),
                ('primera_seccion_contenido', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='contenido')),
                ('covid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.covid', verbose_name='Covid')),
            ],
            options={
                'verbose_name': 'Comunicado',
                'verbose_name_plural': 'Comunicados',
            },
        ),
    ]