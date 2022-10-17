# Generated by Django 3.2.16 on 2022-10-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_auto_20221014_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='centrodeayuda',
            old_name='tercera_seccion_boton_principal',
            new_name='segunda_seccion_boton_principal',
        ),
        migrations.RenameField(
            model_name='centrodeayuda',
            old_name='tercera_seccion_boton_principal_url',
            new_name='segunda_seccion_boton_principal_url',
        ),
        migrations.RenameField(
            model_name='centrodeayuda',
            old_name='tercera_seccion_preguntas',
            new_name='segunda_seccion_preguntas',
        ),
        migrations.RenameField(
            model_name='centrodeayuda',
            old_name='cuarta_seccion_alt_imagen',
            new_name='tercera_seccion_alt_imagen',
        ),
        migrations.RenameField(
            model_name='centrodeayuda',
            old_name='cuarta_seccion_imagen',
            new_name='tercera_seccion_imagen',
        ),
        migrations.RenameField(
            model_name='centrodeayuda',
            old_name='cuarta_seccion_titulo_imagen',
            new_name='tercera_seccion_titulo_imagen',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='cuarta_seccion_ocultar',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='etiqueta_email_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='etiqueta_mensaje_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='etiqueta_nombre_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='etiqueta_telefono_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='etiqueta_tipo_de_negocio_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='formulario_boton_principal_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='formulario_descripcion_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='formulario_titulo_contacto',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='tercera_seccion_descripcion',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='tercera_seccion_destacado',
        ),
        migrations.RemoveField(
            model_name='centrodeayuda',
            name='tercera_seccion_titulo',
        ),
        migrations.AddField(
            model_name='banner',
            name='segundo_boton',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='segundo botón'),
        ),
        migrations.AddField(
            model_name='banner',
            name='segundo_boton_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='url del segundo botón'),
        ),
    ]
