# Generated by Django 3.2.16 on 2022-10-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20221014_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypymes',
            name='segunda_seccion_boton',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='botón'),
        ),
        migrations.AddField(
            model_name='mypymes',
            name='segunda_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='about',
            name='cuarta_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='about',
            name='primera_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='about',
            name='quinta_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='about',
            name='tercera_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='accion',
            name='boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='segunda_seccion_url_primer_boton',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del primer botón'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='segunda_seccion_url_segundo_boton',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del segundo botón'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='centrodeayuda',
            name='primera_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='centrodeayuda',
            name='tercera_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='covid',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='covid',
            name='primera_seccion_video_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del video'),
        ),
        migrations.AlterField(
            model_name='dhl',
            name='cuarta_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='dhl',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='cuarta_seccion_primer_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del primer botón'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='cuarta_seccion_segundo_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del segundo botón'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='quinta_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='tercera_seccion_enlace_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del enlace'),
        ),
        migrations.AlterField(
            model_name='enviosinternacionales',
            name='cuarta_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='enviosinternacionales',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='enviosinternacionales',
            name='quinta_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='enviosinternacionales',
            name='tercera_seccion_boton_url_primer_bloque',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del primer bloque'),
        ),
        migrations.AlterField(
            model_name='enviosinternacionales',
            name='tercera_seccion_boton_url_segundo_bloque',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del segundo bloque'),
        ),
        migrations.AlterField(
            model_name='enviosnacionales',
            name='cuarta_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='enviosnacionales',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='enviosnacionales',
            name='tercera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='enviosnacionalesrecomendaciones',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='home',
            name='cuarta_seccion_tarjeta_1_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='home',
            name='cuarta_seccion_tarjeta_2_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='home',
            name='primera_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón principal'),
        ),
        migrations.AlterField(
            model_name='home',
            name='primera_seccion_boton_secundario_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón secundario'),
        ),
        migrations.AlterField(
            model_name='home',
            name='primera_seccion_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='enlace'),
        ),
        migrations.AlterField(
            model_name='home',
            name='quinta_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='home',
            name='segunda_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón principal'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tercera_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón principal'),
        ),
        migrations.AlterField(
            model_name='miprimerenvio',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='mypymes',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='mypymes',
            name='primera_seccion_video',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='mypymes',
            name='septima_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='mypymes',
            name='sexta_seccion_primer_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del primer botón'),
        ),
        migrations.AlterField(
            model_name='mypymes',
            name='sexta_seccion_segundo_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del segundo botón'),
        ),
        migrations.AlterField(
            model_name='mypymes',
            name='tercera_seccion_enlace_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del enlace'),
        ),
        migrations.AlterField(
            model_name='opcion',
            name='boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='reclamos',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='reclamos',
            name='tercera_seccion_enlace_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del enlace'),
        ),
        migrations.AlterField(
            model_name='recomendacionesembalaje',
            name='primera_seccion_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='cuarta_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='tercera_seccion_tarjeta_1_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='tercera_seccion_tarjeta_2_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='seguimientoindicaciones',
            name='enlace_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del enlace'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
        migrations.AlterField(
            model_name='starkenpro',
            name='primera_seccion_boton_principal_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del botón'),
        ),
    ]