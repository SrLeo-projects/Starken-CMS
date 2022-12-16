from datetime import datetime
from enum import unique
import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from faicon.fields import FAIconField


class CustomImage(models.ImageField):
    def __init__(self, *args, **kwargs):
        super(CustomImage, self).__init__(*args, **kwargs)
        
    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if(value):
            img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/'+ value)
            img = Image.open(img_path)
            file_size = os.path.getsize(img_path)
            print(file_size)
            file_size_kb = file_size/1000
            print(file_size_kb)
            if file_size_kb > 200: 
                if img.filename.split('.')[1] == 'png':
                    bg = Image.new("RGB", img.size, (255,255,255))
                    bg.paste(img, (0,0), img)
                    porcentaje = int(48000/file_size_kb)
                    img = bg.save(fp=os.path.join("media/", value + ".jpg"), optimize=True, quality=porcentaje)
                    os.remove('media/'+ value)
                    return value.replace(".png", ".jpg")
                else:
                    porcentaje = int(142500/file_size_kb)
                    img = img.save(img_path, optimize=True, quality=porcentaje)
                    return value
            else:
                return value

class Tipo(models.TextChoices):
    ADVERTENCIA = "ADVERTENCIA", "ADVERTENCIA"
    APROBADO = "APROBADO", "APROBADO"
    URGENTE = "URGENTE", "URGENTE"
    
    def color_class(self):
        if self.value == 'ADVENTENCIA':
            return 'warning'
        elif self.value == 'APROBADO':
            return 'primary'
        elif self.value == 'URGENTE':
            return 'danger'
class Notificacion(models.Model):
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    fecha_de_caducidad = models.DateField(verbose_name='fecha de caducidad', null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=Tipo.choices, null=True, blank=True, default=Tipo.ADVERTENCIA, verbose_name='Tipo')
    
    def get_tipo_color_class(self):
        return Tipo(self.value).color_class()
    
    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
    
class NotificacionModal(models.Model):
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='notificacion_modal', verbose_name='imagen', null=True, blank=True)
    fecha_de_caducidad = models.DateField(verbose_name='fecha de caducidad', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Notificación Modal'
        verbose_name_plural = 'Notificación Modal'   
    
class URL(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='nombre de la URL', null=True, blank=True)
    url = models.CharField(max_length=255, verbose_name='URL', null=True, blank=True)
    
    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URL'
    
    def __str__(self):
            return f'{self.nombre} - {self.url}'

class BaseModel(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    class Meta:
        abstract = True

class Servicio(BaseModel):
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='servicios', verbose_name='imagen', null=True, blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_servicio', null=True, blank=True)

    class Meta:
        verbose_name = 'servicio'

class Home(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    primera_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    primera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='url_boton_principal', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='url_boton_secundario', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_subtitulo_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_link = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    primera_seccion_link_texto = models.CharField(max_length=255, verbose_name='texto del enlace', null=True, blank=True)

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    segunda_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    segunda_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='segunda_url_boton_principal', null=True, blank=True)
    segunda_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    segunda_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='url_boton_secundario_segunda_seccion', null=True, blank=True)

    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='seguimiento', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    tercera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='tercera_url_boton_principal', null=True, blank=True)
    tercera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    tercera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='url_boton_secundario_tercera_seccion', null=True, blank=True)

    cuarta_seccion_tarjeta_1_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_1_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón tarjeta 1', related_name='url_boton_tarjeta_1', null=True, blank=True)

    cuarta_seccion_tarjeta_2_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_2_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón tarjeta 2', related_name='url_boton_tarjeta_2', null=True, blank=True)

    quinta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    quinta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_palabras = models.CharField(max_length=255, verbose_name='palabras', help_text='separadas por coma', null=True, blank=True)
    quinta_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)

    quinta_seccion_app_store_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='enlace playstore', related_name='quinta_url_boton_principal', null=True, blank=True)
    quinta_seccion_google_play_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='enlace appstore', related_name='url_boton_secundario_quinta_seccion', null=True, blank=True)

    servicios = models.ManyToManyField(Servicio, verbose_name='servicios', blank=True)
    
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    quinta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")

    class Meta:
        verbose_name_plural = 'home'
    
    
    def titulo_destacado(self, seccion):
        return self.__dict__[f'{seccion}_seccion_titulo'].replace(self.__dict__[f'{seccion}_seccion_destacado'], f'<strong class="fw-bold text-primary">{self.__dict__[f"{seccion}_seccion_destacado"]}</strong>')

# Banner -> HomeBanner
class Banner(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='carousel', null=True, blank=True)

    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='carousel', verbose_name='imagen', null=True, blank=True)
    titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)

    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_boton', null=True, blank=True)
    segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segundo_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_boton', null=True, blank=True)
    titulo_corto = models.CharField(max_length=255, verbose_name='título corto', null=True, blank=True)
    descripcion_corta = models.CharField(max_length=255, verbose_name='descripción corta', null=True, blank=True)

    

# Option -> HomeOption
class Opcion(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='opciones', null=True, blank=True)

    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='opciones', verbose_name='imagen', null=True, blank=True)

    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton', null=True, blank=True)

    class Meta:
        verbose_name = 'opción'
        verbose_name_plural = 'opciones'


# SOMOS STARKEN

class About(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='about', verbose_name='imagen', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='primera_url_boton_principal_about', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='about_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='tercera_url_boton_principal_about', null=True, blank=True)
    tercera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    tercera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='about_url_boton_secundario_tercera_seccion', null=True, blank=True)
   
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='cuarta_url_boton_principal_about', null=True, blank=True)
    cuarta_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    cuarta_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='about_url_boton_secundario_cuarta_seccion', null=True, blank=True)

    quinta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    quinta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='about', verbose_name='imagen', null=True, blank=True)
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    quinta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    quinta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='quinta_url_boton_principal_about', null=True, blank=True)
    quinta_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    quinta_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='about_url_boton_secundario_quinta_seccion', null=True, blank=True)
   
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    quinta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")

    class Meta:
        verbose_name = 'somos STARKEN'
        verbose_name_plural = 'somos STARKEN'
    

    

# Agregar más campos en base a https://desa.sbmundo.com/starken/responsabilidad-social.html
# TODO revisar campos de artículos


class Articulo(BaseModel):
    class Tipo(models.TextChoices):
        NOTICIA = 'noticia', 'Noticia'
        RESPONSABILIDAD_SOCIAL = 'responsabilidad social', 'Responsabilidad social'
        SUSTENTABILIDAD = 'sustentabilidad', 'Sustentabilidad'
    
    tipo = models.CharField(max_length=255, choices=Tipo.choices, verbose_name='tipo', null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True) 
    primera_seccion_etiqueta = models.CharField(max_length=255, verbose_name='etiqueta', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_fecha_de_creacion = models.DateField(verbose_name='fecha de creación', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='articles', verbose_name='imagen', null=True, blank=True)
    primera_seccion_contenido = RichTextUploadingField(verbose_name='contenido', null=True, blank=True)
    fecha_de_actualizacion = models.DateField(verbose_name='fecha de actualización', null=True, blank=True)
    
    segunda_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    segunda_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    segunda_seccion_imagen = models.ImageField(upload_to='articles', verbose_name='imagen', null=True, blank=True)
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    segunda_seccion_url_primer_boton = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_boton_articulo', null=True, blank=True)
    segunda_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segunda_seccion_url_segundo_boton = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_boton_articulo', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    

    class Meta:
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)
    
        
        
# Starken PRO
class StarkenPro(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)
    primera_seccion_primer_titulo = models.CharField(max_length=255, verbose_name='primer título', null=True, blank=True)
    primera_seccion_primera_descripcion = RichTextField(verbose_name='Primera descripción', null=True, blank=True)
    primera_seccion_segundo_titulo = models.CharField(max_length=255, verbose_name='segundo título', null=True, blank=True)
    primera_seccion_segunda_descripcion = RichTextField(verbose_name='Segunda descripción', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='url_boton_principal_starkenpro', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='starkenpro_url_boton_secundario_primera_seccion', null=True, blank=True)

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    cuarta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_video = models.URLField(verbose_name='video', null=True, blank=True)
    
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")

    class Meta:
        verbose_name = 'starken PRO'
        verbose_name_plural = 'starken PRO'

class StarkenProBeneficio(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    class Meta:
        verbose_name = 'Beneficio'
        verbose_name_plural = 'Beneficios'

class StarkenProPaso(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)
    paso = models.CharField(max_length=255, verbose_name='número de indicación', null=True, blank=True)
    imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    class Meta:
        verbose_name = 'Indicaciones'
        verbose_name_plural = 'Indicaciones'

#Preguntas Frecuentes
class PreguntasCategoria(models.Model):
    titulo_categoria = models.CharField(max_length=255, verbose_name='Título de categoría', null=True, blank=True)
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    imagen = models.ImageField(upload_to='preguntas', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'FAQ - Categoría'
        verbose_name_plural = 'FAQ - Categoría'
        
    def __str__(self):
            return self.titulo_categoria
    
    
class Preguntas(models.Model):
    pregunta = models.ForeignKey(PreguntasCategoria, on_delete=models.CASCADE, related_name='preguntas',  verbose_name='Preguntas', null=True, blank=True)
    pregunta_titulo = models.CharField(max_length=255, verbose_name='pregunta título', null=True, blank=True)
    pregunta_descripcion = RichTextField(verbose_name='pregunta descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    
    def __str__(self):
        return self.pregunta_titulo
    

class PreguntasFrecuentes(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_boton_buscar = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    
    segunda_seccion_preguntas = models.ManyToManyField(Preguntas, verbose_name='Preguntas', blank=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    tercera_seccion_icono_primer_bloque = FAIconField(verbose_name='ícono primer bloque', null=True, blank=True)
    tercera_seccion_titulo_primer_bloque = models.CharField(max_length=255, verbose_name='título primer bloque', null=True, blank=True)
    tercera_seccion_descripcion_primer_bloque = models.TextField(verbose_name='descripción primer bloque', null=True, blank=True)
    tercera_seccion_url_primer_bloque = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url botón primer bloque', related_name='url_tercera_seccion_primer_bloque', null=True, blank=True)
    
    tercera_seccion_icono_segundo_bloque = FAIconField(verbose_name='ícono segundo bloque', null=True, blank=True)
    tercera_seccion_titulo_segundo_bloque = models.CharField(max_length=255, verbose_name='título segundo bloque', null=True, blank=True)
    tercera_seccion_descripcion_segundo_bloque = models.TextField(verbose_name='descripción segundo bloque', null=True, blank=True)
    tercera_seccion_url_segundo_bloque = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url botón segundo bloque', related_name='url_tercera_seccion_segundo_bloque', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
    
    

      
#Help Center
class CentrodeAyuda(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='primera_url_boton_principal_centro_de_ayuda', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='centro_de_ayuda_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    segunda_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    segunda_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='segunda_url_boton_principal_centro_de_ayuda', null=True, blank=True)
    segunda_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    segunda_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='centro_de_ayuda_url_boton_secundario_segunda_seccion', null=True, blank=True)
    segunda_seccion_preguntas = models.ManyToManyField(Preguntas, verbose_name='Preguntas', blank=True)
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    formulario_subtitulo = RichTextField(verbose_name='subtitulo', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='email', null=True, blank=True)
    etiqueta_orden_de_flete = models.CharField(max_length=255, verbose_name='número de orden de flete', null=True, blank=True)
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='mensaje', null=True, blank=True)
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='CentrodeAyuda', verbose_name='imagen', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'centro de ayuda'
        verbose_name_plural = 'centro de ayuda'
    

    
    
class CentrodeAyudaBeneficio(BaseModel):
    centro_de_ayuda = models.ForeignKey(CentrodeAyuda, on_delete=models.CASCADE, verbose_name='Centro de Ayuda', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    image = models.ImageField(upload_to='centro_de_ayuda', verbose_name='imagen', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextUploadingField(blank=True, verbose_name='descripción', null=True)
    url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='URL', related_name='url_centro_de_ayuda_beneficio', null=True, blank=True)
    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'


#Condiciones de Servicio
class TerminosdeServicio(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_descripcion = RichTextField(blank=True, verbose_name='descripción', null=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Condición de Servicio'
        verbose_name_plural = 'Condiciones de Servicio'
class TerminosdeServicioSeccion(models.Model):
    terminos_de_servicio = models.ForeignKey(TerminosdeServicio, on_delete=models.CASCADE, verbose_name='Términos de Servicio', null=True, blank=True)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='id')
    seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Nueva Sección'
        verbose_name_plural = 'Nueva Sección'
    
class TerminosdeServicioPunto(models.Model):
    terminos_de_servicio = models.ForeignKey(TerminosdeServicio, on_delete=models.CASCADE, verbose_name='Términos de Servicio', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título de término', null=True, blank=True)
    descripcion = RichTextField(verbose_name='descripción de término', null=True, blank=True)
    class Meta:
        verbose_name = 'Punto de Condición de Servicio'
        verbose_name_plural = 'Puntos de Condiciones de Servicio'
        
#Contactanos
class Contactanos(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='contactanos', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='primera_url_boton_principal_contactanos', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='contactanos_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    
    segunda_seccion_icon_whatsapp = FAIconField(verbose_name='ícono whatsapp', null=True, blank=True)
    segunda_seccion_url_whatsapp = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url de whatsapp', related_name='url_whatsapp', null=True, blank=True)
    segunda_seccion_titulo_whatsapp = models.CharField(max_length=255, verbose_name='título whatsapp', null=True, blank=True)
    segunda_seccion_descripcion_whatsapp = RichTextField(verbose_name='descripción whatsapp', null=True, blank=True)
    segunda_seccion_icon_telefono = FAIconField(verbose_name='ícono teléfono', null=True, blank=True)
    segunda_seccion_titulo_telefono = models.CharField(max_length=255, verbose_name='título teléfono', null=True, blank=True)
    segunda_seccion_descripcion_telefono = RichTextField(verbose_name='descripción teléfono', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    
    
    
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='contactanos', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario', null=True, blank=True)
    tercera_seccion_formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario', null=True, blank=True)
    tercera_seccion_etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    tercera_seccion_etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    tercera_seccion_etiqueta_comentario = models.CharField(max_length=255, verbose_name='etiqueta comentario', null=True, blank=True)
    
    cuarta_seccion_tarjeta_1_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_imagen = models.ImageField(upload_to='contactanos', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_1_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón tarjeta 1', related_name='url_boton_tarjeta_1_contactanos', null=True, blank=True)

    cuarta_seccion_tarjeta_2_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_imagen = models.ImageField(upload_to='contactanos', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_2_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón tarjeta 2', related_name='url_boton_tarjeta_2_contactanos', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Contáctanos'
        verbose_name_plural = 'Contáctanos'
    
        
class RedSocial(models.Model):
    class TipoRed(models.TextChoices):
        INSTAGRAM = 'instagram', 'instagram'
        FACEBOOK = 'facebook', 'facebook'
        TWITTER = 'twitter', 'twitter'
        YOUTUBE = 'youtube', 'youtube'
        LINKEDIN = 'linkedin', 'linkedin'
    
    red_social = models.CharField(max_length=255, choices=TipoRed.choices, verbose_name='red social', null=True, blank=True)
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto', null=True, blank=True)
    
    boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_red_social', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Redes Sociales'
        verbose_name_plural = 'Redes Sociales'

       
#
class Cotizador(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    etiqueta_origen = models.CharField(max_length=255, verbose_name='etiqueta origen', null=True, blank=True)
    etiqueta_destino = models.CharField(max_length=255, verbose_name='etiqueta destino', null=True, blank=True)
    etiqueta_encomienda = models.CharField(max_length=255, verbose_name='etiqueta encomienda', null=True, blank=True)
    etiqueta_dimensiones = models.CharField(max_length=255, verbose_name='etiqueta dimensiones', null=True, blank=True)
    etiqueta_peso = models.CharField(max_length=255, verbose_name='etiqueta peso', null=True, blank=True)
    etiqueta_servicio = models.CharField(max_length=255, verbose_name='etiqueta servicio', null=True, blank=True)
    etiqueta_tipo_de_entrega = models.CharField(max_length=255, verbose_name='etiqueta tipo de entrega', null=True, blank=True)
    boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    segunda_seccion_boton_principal_destacado = models.CharField(max_length=255, verbose_name='destacado botón principal', null=True, blank=True)
    segunda_seccion_advertencia = models.CharField(max_length=255, verbose_name='advertencia', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Cotizador'
        verbose_name_plural = 'Cotizador'
        
class Boton(models.Model):
    cotizador = models.ForeignKey(Cotizador, on_delete=models.CASCADE, verbose_name='Cotizador', null=True, blank=True)
    etiqueta_boton = models.CharField(max_length=255, verbose_name='etiqueta botón', null=True, blank=True)
    destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_cotizador', null=True, blank=True)
    icon = FAIconField(verbose_name='ícono', null=True, blank=True)
    class Meta:
        verbose_name = 'Botón'
        verbose_name_plural = 'Botones'

class ImagenCarrusel(models.Model):
    cotizador = models.ForeignKey(Cotizador, on_delete=models.CASCADE, verbose_name='Cotizador', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='cotizador', verbose_name='imagen', null=True, blank=True)
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        
class Advertencia(models.Model):
    cotizador = models.ForeignKey(Cotizador, on_delete=models.CASCADE, verbose_name='Cotizador', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    class Meta:
        verbose_name = 'Advertencia'
        verbose_name_plural = 'Advertencias'
        

#DHL
class DHL(BaseModel):
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_principal_dhl', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='dhl_url_boton_secundario_primera_seccion', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='dhl', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    

    tercera_seccion_contenido = RichTextField(verbose_name='contenido', null=True, blank=True)
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='cuarta_url_boton_principal_dhl', null=True, blank=True)
    cuarta_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    cuarta_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='dhl_url_boton_secundario_cuarta_seccion', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'DHL'
        verbose_name_plural = 'DHL'
          

class Modalidades(models.Model):
    modalidad = models.ForeignKey(DHL, on_delete=models.CASCADE, verbose_name='Modalidad', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='dhl', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextUploadingField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Modalidades de Servicio'
        verbose_name_plural = 'Modalidades de Servicio'
       
class Accion(models.Model):
    accion = models.ForeignKey(DHL, on_delete=models.CASCADE, verbose_name='Acción', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='dhl', verbose_name='imagen', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_accion', null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Acciones'
        verbose_name_plural = 'Acciones'
       
#Empresas
class Empresas(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_empresas', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='empresas_url_boton_secundario_primera_seccion', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_titulo_imagen_fondo = models.CharField(max_length=255, verbose_name='título imagen de fondo', null=True, blank=True)
    tercera_seccion_alt_imagen_fondo = models.CharField(max_length=255, verbose_name='alt imagen de fondo', null=True, blank=True)
    tercera_seccion_imagen_fondo = models.ImageField(upload_to='empresas', verbose_name='imagen de fondo', null=True, blank=True)
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_rut_empresa = models.CharField(max_length=255, verbose_name='etiqueta rut empresa', null=True, blank=True)
    etiqueta_nombre_contacto = models.CharField(max_length=255, verbose_name='etiqueta nombre contacto', null=True, blank=True)
    etiqueta_razon_social = models.CharField(max_length=255, verbose_name='etiqueta razón social', null=True, blank=True)
    etiqueta_rut_contacto = models.CharField(max_length=255, verbose_name='etiqueta rut contacto', null=True, blank=True)
    etiqueta_direccion = models.CharField(max_length=255, verbose_name='etiqueta dirección', null=True, blank=True)
    etiqueta_email_contacto = models.CharField(max_length=255, verbose_name='etiqueta email contacto', null=True, blank=True)
    etiqueta_comuna = models.CharField(max_length=255, verbose_name='etiqueta comuna', null=True, blank=True)
    etiqueta_telefono_contacto = models.CharField(max_length=255, verbose_name='etiqueta teléfono contacto', null=True, blank=True)
    etiqueta_rubro = models.CharField(max_length=255, verbose_name='etiqueta rubro', null=True, blank=True)
    etiqueta_comentario = models.CharField(max_length=255, verbose_name='etiqueta comentario', null=True, blank=True)
    
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='logo', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    tercera_seccion_enlace = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    tercera_seccion_enlace_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del enlace', related_name='url_enlace_empresas', null=True, blank=True)
    tercera_seccion_titulo_carrusel = models.CharField(max_length=255, verbose_name='título de carrusel', null=True, blank=True)
    
    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_descripcion = RichTextField(blank=True, verbose_name='descripción', null=True)
    cuarta_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    cuarta_seccion_primer_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_boton_empresas', null=True, blank=True)
    cuarta_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    cuarta_seccion_segundo_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_boton_empresas', null=True, blank=True)
    
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    quinta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='quinta_url_boton_empresas', null=True, blank=True)
    quinta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    quinta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='imagen', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    quinta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
       
class EmpresasBeneficios(models.Model):
    beneficio = models.ForeignKey(Empresas, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='empresas', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextUploadingField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
       

class EmpresasCarrusel(models.Model):
    beneficio = models.ForeignKey(Empresas, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='empresas', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Imágenes'
        verbose_name_plural = 'Imágenes'
       


#Envíos internacionales
class EnviosInternacionales(BaseModel):
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_envios_internacionales', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='internacionales_url_boton_secundario_primera_seccion', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='envios internacionales', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_titulo_imagen_primer_bloque = models.CharField(max_length=255, verbose_name='título imagen primer bloque', null=True, blank=True)
    tercera_seccion_alt_imagen_primer_bloque = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen_primer_bloque = models.ImageField(upload_to='envios internacionales', verbose_name='imagen de fondo primer bloque', null=True, blank=True)
    tercera_seccion_titulo_primer_bloque = models.CharField(max_length=255, verbose_name='título primer bloque', null=True, blank=True)
    tercera_seccion_descripcion_primer_bloque = models.TextField(blank=True, verbose_name='descripción primer bloque', null=True)
    tercera_seccion_boton_primer_bloque = models.CharField(max_length=255, verbose_name='botón primer bloque', null=True, blank=True)
    tercera_seccion_boton_url_primer_bloque = models.CharField(max_length=255, verbose_name='url del primer bloque', null=True, blank=True)
    tercera_seccion_titulo_imagen_segundo_bloque = models.CharField(max_length=255, verbose_name='título imagen segundo bloque', null=True, blank=True)
    tercera_seccion_alt_imagen_segundo_bloque = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen_segundo_bloque = models.ImageField(upload_to='envios internacionales', verbose_name='imagen de fondo segundo bloque', null=True, blank=True)
    tercera_seccion_titulo_segundo_bloque = models.CharField(max_length=255, verbose_name='título segundo bloque', null=True, blank=True)
    tercera_seccion_descripcion_segundo_bloque = models.TextField(blank=True, verbose_name='descripción segundo bloque', null=True)
    tercera_seccion_boton_segundo_bloque = models.CharField(max_length=255, verbose_name='botón segundo bloque', null=True, blank=True)
    tercera_seccion_boton_url_segundo_bloque = models.CharField(max_length=255, verbose_name='url del segundo bloque', null=True, blank=True)
    
    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='envios internacionales', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='cuarta_url_boton_envios_internacionales', null=True, blank=True)
    cuarta_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    cuarta_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='internacionales_url_boton_secundario_cuarta_seccion', null=True, blank=True)
    
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    quinta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='quinta_url_boton_envios_internacionales', null=True, blank=True)
    quinta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    quinta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='envios internacionales', verbose_name='imagen', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    quinta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Envíos Internacionales'
        verbose_name_plural = 'Envíos Internacionales'
        
       
class EnviosInternacionalesBeneficios(models.Model):
    beneficio = models.ForeignKey(EnviosInternacionales, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios internacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'



#Envíos Nacionales
class EnviosNacionales(BaseModel):
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_envios_nacionales', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='nacionales_url_boton_secundario_primera_seccion', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='tercera_url_boton_envios_nacionales', null=True, blank=True)
    tercera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    tercera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='nacionales_url_boton_secundario_tercera_seccion', null=True, blank=True)
    
    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='cuarta_url_boton_envios_nacionales', null=True, blank=True)
    cuarta_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    cuarta_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='nacionales_url_boton_secundario_cuarta_seccion', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Envíos Nacionales'
        verbose_name_plural = 'Envíos Nacionales'
       
class EnviosNacionalesBeneficios(models.Model):
    beneficio = models.ForeignKey(EnviosNacionales, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios nacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
       

class EnviosNacionalesRecomendaciones(models.Model):
    recomendacion = models.ForeignKey(EnviosNacionales, on_delete=models.CASCADE, verbose_name='Recomendaciones', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios nacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    url = models.CharField(max_length=255, verbose_name='url', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Recomendaciones'
        verbose_name_plural = 'Recomendaciones'
       


#Mi Primer Envío
class MiPrimerEnvio(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_mi_primer_envio', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='mi_primer_envio_url_boton_secundario_primera_seccion', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen de fondo', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    
    class Meta:
        verbose_name = 'Mi Primer Envío'
        verbose_name_plural = 'Mi Primer Envío'
       
class MiPrimerEnvioStep(models.Model):
    beneficio = models.ForeignKey(MiPrimerEnvio, on_delete=models.CASCADE, verbose_name='Step', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios nacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_mi_primer_envio_step', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Indicaciones'
        verbose_name_plural = 'Indicaciones'


#Mypymes
class Mypymes(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_mypymes', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='mypymes_url_boton_secundario_primera_seccion', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen de fondo móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen de fondo móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen de fondo móvil', null=True, blank=True)
    primera_seccion_video = models.URLField(verbose_name='video', null=True, blank=True)
    primera_seccion_titulo_imagen_miniatura = models.CharField(max_length=255, verbose_name='título imagen miniatura', null=True, blank=True)
    primera_seccion_alt_imagen_miniatura = models.CharField(max_length=255, verbose_name='alt imagen miniatura', null=True, blank=True)
    primera_seccion_miniatura = models.ImageField(upload_to='mypymes', verbose_name='imagen miniatura', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_titulo_imagen_fondo = models.CharField(max_length=255, verbose_name='título imagen de fondo', null=True, blank=True)
    tercera_seccion_alt_imagen_fondo = models.CharField(max_length=255, verbose_name='alt imagen de fondo', null=True, blank=True)
    tercera_seccion_imagen_fondo = models.ImageField(upload_to='mypymes', verbose_name='imagen de fondo', null=True, blank=True)
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_tipo_de_cliente = models.CharField(max_length=255, verbose_name='etiqueta tipo de cliente', null=True, blank=True)
    etiqueta_rut = models.CharField(max_length=255, verbose_name='etiqueta rut', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre completo', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_telefono = models.CharField(max_length=255, verbose_name='etiqueta teléfono', null=True, blank=True)
    etiqueta_fecha_de_nacimiento = models.CharField(max_length=255, verbose_name='etiqueta fecha de nacimiento', null=True, blank=True)
    etiqueta_direccion = models.CharField(max_length=255, verbose_name='etiqueta dirección', null=True, blank=True)
    etiqueta_comuna = models.CharField(max_length=255, verbose_name='etiqueta comuna', null=True, blank=True)
    etiqueta_rubro = models.CharField(max_length=255, verbose_name='etiqueta rubro', null=True, blank=True)
    etiqueta_envios_mensuales = models.CharField(max_length=255, verbose_name='etiqueta envíos mensuales', null=True, blank=True)
    etiqueta_producto = models.CharField(max_length=255, verbose_name='etiqueta producto que comercializa', null=True, blank=True)
    etiqueta_url_facebook = models.CharField(max_length=255, verbose_name='etiqueta url facebook', null=True, blank=True)
    etiqueta_url_instagram = models.CharField(max_length=255, verbose_name='etiqueta url instagram', null=True, blank=True)
    etiqueta_dls_cajero = models.CharField(max_length=255, verbose_name='etiqueta login usuario dls cajero', null=True, blank=True)
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_titulo_derecho = models.CharField(max_length=255, verbose_name='título lado derecho', null=True, blank=True)
    tercera_seccion_destacado_derecho = models.CharField(max_length=255, verbose_name='destacado lado derecho', null=True, blank=True)
    
    zona_partner_seccion_titulo_logo = models.CharField(max_length=255, verbose_name='título logo', null=True, blank=True)
    zona_partner_seccion_alt_logo = models.CharField(max_length=255, verbose_name='alt logo', null=True, blank=True)
    zona_partner_seccion_logo = models.ImageField(upload_to='mypymes', verbose_name='logo', null=True, blank=True)
    zona_partner_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    zona_partner_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    zona_partner_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    zona_partner_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    
    
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    quinta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    quinta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    quinta_seccion_video = models.URLField(verbose_name='video', null=True, blank=True)
    
    sexta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    sexta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    sexta_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    sexta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    sexta_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    sexta_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    sexta_seccion_primer_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_boton_mypymes', null=True, blank=True)
    sexta_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    sexta_seccion_segundo_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_boton_mypymes', null=True, blank=True)
    
    septima_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    septima_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    septima_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    septima_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='septima_url_boton_mypymes', null=True, blank=True)
    septima_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    septima_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    septima_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    quinta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    sexta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    septima_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'MYPYMES'
        verbose_name_plural = 'MYPYMES'
       
class MypymesBeneficios(models.Model):
    beneficio = models.ForeignKey(Mypymes, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='mypymes', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextUploadingField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'

       
       
#Reclamos

class Reclamos(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='reclamos', verbose_name='imagen', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_reclamos', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='reclamos_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    formulario_primer_titulo = models.CharField(max_length=255, verbose_name='primer título formulario', null=True, blank=True)
    formulario_segundo_titulo = models.CharField(max_length=255, verbose_name='segundo título formulario', null=True, blank=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_tipo_reclamo = models.CharField(max_length=255, verbose_name='etiqueta tipo de reclamo', null=True, blank=True)
    valor_orden_de_flete = models.CharField(max_length=255, verbose_name='valor orden de flete', null=True, blank=True)
    valor_atencion_al_cliente = models.CharField(max_length=255, verbose_name='valor atención al cliente', null=True, blank=True)
    etiqueta_numero_orden_de_flete = models.CharField(max_length=255, verbose_name='etiqueta número orden de flete', null=True, blank=True)
    etiqueta_inconveniente = models.CharField(max_length=255, verbose_name='etiqueta inconveniente', null=True, blank=True)
    etiqueta_tipo_cliente = models.CharField(max_length=255, verbose_name='etiqueta tipo de cliente', null=True, blank=True)
    valor_destinatario = models.CharField(max_length=255, verbose_name='valor destinatario', null=True, blank=True)
    valor_remitente = models.CharField(max_length=255, verbose_name='valor remitente', null=True, blank=True)
    etiqueta_rut = models.CharField(max_length=255, verbose_name='etiqueta rut', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_apellido_paterno = models.CharField(max_length=255, verbose_name='etiqueta apellido paterno', null=True, blank=True)
    etiqueta_apellido_materno = models.CharField(max_length=255, verbose_name='etiqueta apellido materno', null=True, blank=True)
    etiqueta_telefono_fijo = models.CharField(max_length=255, verbose_name='etiqueta teléfono fijo', null=True, blank=True)
    etiqueta_telefono_celular = models.CharField(max_length=255, verbose_name='etiqueta teléfono celular', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_direccion = models.CharField(max_length=255, verbose_name='etiqueta dirección', null=True, blank=True)
    etiqueta_reclamo = models.CharField(max_length=255, verbose_name='etiqueta reclamo', null=True, blank=True)
    primera_notificacion = models.CharField(max_length=255, verbose_name='primera notificación', null=True, blank=True)
    mensaje= models.CharField(max_length=255, verbose_name='mensaje', null=True, blank=True)
    segunda_notificacion = models.CharField(max_length=255, verbose_name='segunda notificación', null=True, blank=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    tercera_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='reclamos_url_boton_tercera_seccion', null=True, blank=True)
    tercera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    tercera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='reclamos_url_boton_secundario_tercera_seccion', null=True, blank=True)
    tercera_seccion_preguntas = models.ManyToManyField(Preguntas, verbose_name='Preguntas', blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Centro de Contacto'
        verbose_name_plural = 'Centro de Contacto'
       
       
       
#Recomendaciones de Embalaje

class RecomendacionesCategoria(BaseModel):
    titulo_categoria = models.CharField(max_length=255, verbose_name='Título de categoría', null=True, blank=True)
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    class Meta:
        verbose_name = 'Recomendaciones - Categoría'
        verbose_name_plural = 'Recomendaciones - Categoría'
    
    
class Recomendaciones(models.Model):
    recomendacion = models.ForeignKey(RecomendacionesCategoria, on_delete=models.CASCADE, related_name='recomendaciones',  verbose_name='Recomendaciones', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='recomendaciones', verbose_name='imagen', null=True, blank=True)
    recomendacion_titulo = models.CharField(max_length=255, verbose_name='recomendación título', null=True, blank=True)
    recomendacion_descripcion = models.TextField(verbose_name='recomendación descripción', null=True, blank=True)
    recomendacion_activo = models.BooleanField(verbose_name='recomendación activa', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Recomendación'
        verbose_name_plural = 'Recomendaciones'


class RecomendacionesEmbalaje(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='recomendaciones de embalaje', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_recomendaciones_embalaje', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='recomendaciones_embalaje_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Recomendaciones de Embalaje'
        verbose_name_plural = 'Recomendaciones de Embalaje'


#Seguimiento de envío

class Seguimiento(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='seguimiento', verbose_name='imagen de fondo', null=True, blank=True)
    
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    primera_seccion_etiqueta_codigo = models.CharField(max_length=255, verbose_name='etiqueta código', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    tercera_seccion_tarjeta_1_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_tarjeta_1_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_tarjeta_1_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_tarjeta_1_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_tarjeta_1_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_tarjeta_1_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_tarjeta_1_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón 1', related_name='url_boton_1_seguimiento', null=True, blank=True)

    tercera_seccion_tarjeta_2_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_tarjeta_2_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_tarjeta_2_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_tarjeta_2_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_tarjeta_2_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_tarjeta_2_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_tarjeta_2_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón 2', related_name='url_boton_2_seguimiento', null=True, blank=True)

    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='seguimiento', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_palabras = models.CharField(max_length=255, verbose_name='palabras', help_text='separadas por coma', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón PlayStore', null=True, blank=True)
    cuarta_seccion_boton_principal_enlace = models.CharField(max_length=255, verbose_name='enlace PlayStore', null=True, blank=True)
    cuarta_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón AppStore', null=True, blank=True)
    cuarta_seccion_boton_secundario_enlace = models.CharField(max_length=255, verbose_name='enlace AppStore', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Seguimiento de Envío'
        verbose_name_plural = 'Seguimiento de Envío'
       
       
class SeguimientoIndicaciones(models.Model):
    seguimiento = models.ForeignKey(Seguimiento, on_delete=models.CASCADE, verbose_name='Seguimiento', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='seguimiento', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    enlace = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    enlace_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del enlace', related_name='url_enlace_seguimiento', null=True, blank=True)
    class Meta:
        verbose_name = 'Indicaciones'
        verbose_name_plural = 'Indicaciones'
    

       

#Sucursales
class Sucursales(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    bloque_izquierdo_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    bloque_izquierdo_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    bloque_izquierdo_imagen = models.ImageField(upload_to='sucursales', verbose_name='imagen', null=True, blank=True)
    bloque_izquierdo_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    bloque_izquierdo_contenido = RichTextField(verbose_name='contenido', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    bloque_izquierdo_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    class Meta:
        verbose_name = 'Sucursales'
        verbose_name_plural = 'Sucursales'
    
class Covid(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='seguimiento', verbose_name='imagen miniatura', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_covid', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='covid_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Covid-19'
        verbose_name_plural = 'Covid-19'

       
class CovidComunicado(models.Model):
    covid = models.ForeignKey(Covid, on_delete=models.CASCADE, verbose_name='Covid', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    class Meta:
        verbose_name = 'Comunicado'
        verbose_name_plural = 'Comunicados'


class FormularioEmpresa(models.Model):
    rut_empresa = models.CharField(max_length=255, verbose_name='rut empresa', null=True, blank=True)
    rut_contacto = models.CharField(max_length=255, verbose_name='rut contacto', null=True, blank=True)
    nombre_contacto = models.CharField(max_length=255, verbose_name='nombre contacto', null=True, blank=True)
    razon_social = models.CharField(max_length=255, verbose_name='razón social', null=True, blank=True)
    direccion = models.CharField(max_length=255, verbose_name='dirección', null=True, blank=True)
    email = models.EmailField(max_length=255, db_index=True, verbose_name='email contacto', null=True, blank=True)
    comuna = models.CharField(max_length=255, verbose_name='comuna', null=True, blank=True)
    telefono = models.CharField(max_length=255, verbose_name='teléfono contacto', null=True, blank=True)
    rubro = models.CharField(max_length=255, verbose_name='rubro o actividad', null=True, blank=True)
    comentario = models.TextField(verbose_name='comentario', null=True, blank=True)
    class Meta:
        verbose_name = 'Empresas'
        verbose_name_plural = 'Empresa'
     
            
class FormularioMypymes(models.Model):
    class Tipo(models.TextChoices):
        Masculino = 'MASCULINO', 'MASCULINO'
        FEMENINO = 'FEMENINO', 'FEMENINO'
        EMPRESA = 'EMPRESA', 'EMPRESA'
    
    tipo = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.Masculino, verbose_name='tipo cliente')
    rut = models.CharField(max_length=255, verbose_name='rut', null=True, blank=True)
    nombre = models.CharField(max_length=255, verbose_name='nombre', null=True, blank=True)
    email = models.EmailField(max_length=255, db_index=True, verbose_name='correo electrónico', null=True, blank=True)
    telefono = models.CharField(max_length=255, verbose_name='teléfono', null=True, blank=True)
    fecha_nacimiento = models.DateField(default=datetime.now, verbose_name='fecha de nacimiento', null=True, blank=True)
    direccion = models.CharField(max_length=255, verbose_name='dirección', null=True, blank=True)
    comuna = models.CharField(max_length=255, verbose_name='comuna', null=True, blank=True)
    rubro = models.CharField(max_length=255, verbose_name='rubro', null=True, blank=True)
    envios_mensuales = models.CharField(max_length=255, verbose_name='envíos mensuales', null=True, blank=True)
    producto = models.CharField(max_length=255, verbose_name='producto que comercializa', null=True, blank=True)
    url_facebook = models.URLField(max_length=255, verbose_name='url facebook', null=True, blank=True)
    url_instagram = models.URLField(max_length=255, verbose_name='url instagram', null=True, blank=True)
    dls_cajero = models.CharField(max_length=255, verbose_name='login usuario dls cajero', null=True, blank=True)
    
    class Meta:
        verbose_name = 'MYPYMES'
        verbose_name_plural = 'MYPYMES'

#Servicios

class Servicios(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_servicios', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='servicios_url_boton_secundario_primera_seccion', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='servicios', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen de fondo móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen de fondo móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen de fondo móvil', null=True, blank=True)
    
    segunda_seccion_servicios = models.ManyToManyField(Servicio, verbose_name='servicios', blank=True)
    
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='servicios', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    tercera_seccion_primer_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_boton_servicios', null=True, blank=True)
    tercera_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    tercera_seccion_segundo_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_boton_servicios', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'


class ServiciosCarrusel(models.Model):
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, verbose_name='Servicio', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='servicios', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Imágenes'
        verbose_name_plural = 'Imágenes'

class Registro(BaseModel):
    formulario_titulo = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    
    etiqueta_rut = models.CharField(max_length=255, verbose_name='etiqueta rut', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_apellido = models.CharField(max_length=255, verbose_name='etiqueta apellido', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_direccion = models.CharField(max_length=255, verbose_name='etiqueta dirección', null=True, blank=True)
    etiqueta_comuna = models.CharField(max_length=255, verbose_name='etiqueta comuna', null=True, blank=True)
    etiqueta_sucursal = models.CharField(max_length=255, verbose_name='etiqueta sucursal', null=True, blank=True)
    etiqueta_telefono = models.CharField(max_length=255, verbose_name='etiqueta número telefónico', null=True, blank=True)
    etiqueta_movil = models.CharField(max_length=255, verbose_name='etiqueta número móvil', null=True, blank=True)
    etiqueta_contraseña = models.CharField(max_length=255, verbose_name='etiqueta contraseña', null=True, blank=True)
    
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_registro', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='registro_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    cuarta_seccion_tarjeta_1_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_imagen = models.ImageField(upload_to='registro', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_1_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón tarjeta 1', related_name='url_boton_tarjeta_1_registro', null=True, blank=True)

    cuarta_seccion_tarjeta_2_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_imagen = models.ImageField(upload_to='registro', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_2_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón tarjeta 2', related_name='url_boton_tarjeta_2_registro', null=True, blank=True)
   
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    cuarta_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registro'
        
    
class RegistroBeneficios(models.Model):
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, verbose_name='Registro', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='empresas', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios-Registro'
        verbose_name_plural = 'Beneficios-Registro'


class Login(BaseModel):
    formulario_titulo = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    formulario_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario formulario', null=True, blank=True)
    etiqueta_usuario = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_contraseña = models.CharField(max_length=255, verbose_name='etiqueta contraseña', null=True, blank=True)
    
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_login', null=True, blank=True)
    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='login_url_boton_secundario_primera_seccion', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='decripción', null=True, blank=True)
    segunda_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    segunda_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_login_segunda_seccion', null=True, blank=True)
    segunda_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    segunda_seccion_boton_secundario_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón secundario', related_name='login_url_boton_secundario_segunda_seccion', null=True, blank=True)
    segunda_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    segunda_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    segunda_seccion_imagen = models.ImageField(upload_to='login', verbose_name='imagen', null=True, blank=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
   
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Login'
    
class LoginBeneficios(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE, verbose_name='Login', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='login', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='decripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios-Login'
        verbose_name_plural = 'Beneficios-Login'
