# Generated by Django 3.2.15 on 2022-10-07 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20221007_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnviosNacionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('primera_seccion_subtitulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='subtítulo')),
                ('primera_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('primera_seccion_descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('primera_seccion_boton', models.CharField(blank=True, max_length=255, null=True, verbose_name='botón')),
                ('primera_seccion_boton_url', models.URLField(blank=True, null=True, verbose_name='url del botón')),
                ('primera_seccion_imagen', models.ImageField(blank=True, null=True, upload_to='envios nacionales', verbose_name='imagen de fondo')),
                ('segunda_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('segunda_seccion_destacado', models.CharField(blank=True, max_length=255, null=True, verbose_name='destacado')),
                ('segunda_seccion_subtitulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='subtítulo')),
                ('tercera_seccion_imagen', models.ImageField(blank=True, null=True, upload_to='envios nacionales', verbose_name='imagen')),
                ('tercera_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('tercera_seccion_destacado', models.CharField(blank=True, max_length=255, null=True, verbose_name='destacado')),
                ('tercera_seccion_descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('tercera_seccion_boton', models.CharField(blank=True, max_length=255, null=True, verbose_name='botón')),
                ('tercera_seccion_boton_url', models.URLField(blank=True, null=True, verbose_name='url del botón')),
                ('cuarta_seccion_imagen', models.ImageField(blank=True, null=True, upload_to='envios nacionales', verbose_name='imagen')),
                ('cuarta_seccion_titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('cuarta_seccion_destacado', models.CharField(blank=True, max_length=255, null=True, verbose_name='destacado')),
                ('cuarta_seccion_subtitulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='subtítulo')),
                ('cuarta_seccion_boton', models.CharField(blank=True, max_length=255, null=True, verbose_name='botón')),
                ('cuarta_seccion_boton_url', models.URLField(blank=True, null=True, verbose_name='url del botón')),
            ],
            options={
                'verbose_name': 'Envíos Nacionales',
                'verbose_name_plural': 'Envíos Nacionales',
            },
        ),
        migrations.CreateModel(
            name='EnviosNacionalesRecomendaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='envios nacionales', verbose_name='ícono')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('recomendacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.enviosnacionales', verbose_name='Recomendaciones')),
            ],
            options={
                'verbose_name': 'Recomendaciones',
                'verbose_name_plural': 'Recomendaciones',
            },
        ),
        migrations.CreateModel(
            name='EnviosNacionalesBeneficios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='envios nacionales', verbose_name='ícono')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('beneficio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.enviosnacionales', verbose_name='Beneficio')),
            ],
            options={
                'verbose_name': 'Beneficios',
                'verbose_name_plural': 'Beneficios',
            },
        ),
    ]