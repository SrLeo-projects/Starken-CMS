# Generated by Django 3.2.15 on 2022-10-07 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_advertencia_boton_cotizador'),
    ]

    operations = [
        migrations.CreateModel(
            name='DHL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('primera_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('primera_seccion_destacado', models.CharField(blank=True, max_length=255, null=True, verbose_name='destacado')),
                ('primera_seccion_descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('primera_seccion_boton', models.CharField(blank=True, max_length=255, null=True, verbose_name='botón')),
                ('primera_seccion_boton_url', models.URLField(blank=True, null=True, verbose_name='url del botón')),
                ('primera_seccion_imagen', models.ImageField(blank=True, null=True, upload_to='dhl', verbose_name='imagen de fondo')),
                ('segunda_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('segunda_seccion_destacado', models.CharField(blank=True, max_length=255, null=True, verbose_name='destacado')),
                ('segunda_seccion_subtitulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='subtítulo')),
                ('tercera_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('tercera_seccion_subtitulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='subtítulo')),
                ('tercera_seccion_descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('cuarta_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('cuarta_seccion_destacado', models.CharField(blank=True, max_length=255, null=True, verbose_name='destacado')),
                ('cuarta_seccion_descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('cuarta_seccion_boton', models.CharField(blank=True, max_length=255, null=True, verbose_name='botón')),
                ('cuarta_seccion_boton_url', models.URLField(blank=True, null=True, verbose_name='url del botón')),
            ],
            options={
                'verbose_name': 'DHL',
                'verbose_name_plural': 'DHL',
            },
        ),
        migrations.CreateModel(
            name='Modalidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='dhl', verbose_name='ícono')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('modalidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.dhl', verbose_name='Modalidad')),
            ],
            options={
                'verbose_name': 'Modalidades de Servicio',
                'verbose_name_plural': 'Modalidades de Servicio',
            },
        ),
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='dhl', verbose_name='imagen')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('boton', models.CharField(blank=True, max_length=255, null=True, verbose_name='botón')),
                ('boton_url', models.URLField(blank=True, null=True, verbose_name='url del botón')),
                ('accion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.dhl', verbose_name='Acción')),
            ],
            options={
                'verbose_name': 'Acciones',
                'verbose_name_plural': 'Acciones',
            },
        ),
    ]
