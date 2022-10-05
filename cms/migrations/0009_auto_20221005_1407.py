# Generated by Django 3.2.15 on 2022-10-05 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_delete_centrodeayudapregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntascategoria',
            name='titulo_categoria',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Título de categoría'),
        ),
        migrations.CreateModel(
            name='TerminosdeServicioSeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('seccion_descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('terminos_de_servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.terminosdeservicio', verbose_name='Términos de Servicio')),
            ],
            options={
                'verbose_name': 'Nueva Sección',
                'verbose_name_plural': 'Nueva Sección',
            },
        ),
    ]
