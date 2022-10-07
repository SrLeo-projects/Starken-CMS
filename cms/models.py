from enum import unique
import os
from django.db import models
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class CustomImage(models.ImageField):
    def __init__(self, *args, **kwargs):
        super(CustomImage, self).__init__(*args, **kwargs)
        
    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        
        img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/'+ value)
        img = Image.open(img_path)
        file_size = os.path.getsize(img_path)
        print(file_size)
        file_size_kb = file_size/1000
        print(file_size_kb)
        if file_size_kb > 200:
            porcentaje = int(20000/file_size_kb)
            print(porcentaje)
            img.save(img_path,quality=20,optimize=True)
            file_new_size = os.path.getsize(img_path)
            print(file_new_size)
        else:
            img.save(img_path,quality=20,optimize=True)
            file_new_size = os.path.getsize(img_path)
            print(file_new_size)
        return img.filename.split('media/')[1]


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
    boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    class Meta:
        verbose_name = 'servicio'

    def save(self, *args, **kwargs):
       super(Home, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)

class Home(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón principal', null=True, blank=True)

    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.URLField(verbose_name='url del botón secundario', null=True, blank=True)

    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_subtitulo_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    primera_seccion_link = models.URLField(verbose_name='enlace', null=True, blank=True)
    primera_seccion_link_texto = models.CharField(max_length=255, verbose_name='texto del enlace', null=True, blank=True)

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    segunda_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    segunda_seccion_boton_principal_url = models.URLField(verbose_name='url del botón principal', null=True, blank=True)

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    tercera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón principal', null=True, blank=True)

    cuarta_seccion_tarjeta_1_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_1_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    cuarta_seccion_tarjeta_2_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_2_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_2_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_2_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_palabras = models.CharField(max_length=255, verbose_name='palabras', help_text='separadas por coma', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    quinta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    servicios = models.ManyToManyField(Servicio, verbose_name='servicios', blank=True)

    class Meta:
        verbose_name_plural = 'home'
    
       
    def save(self, *args, **kwargs):
       super(Home, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       cuarta_seccion_tarjeta_1_imagen = Image.open(self.cuarta_seccion_tarjeta_1_imagen.path)
       cuarta_seccion_tarjeta_1_imagen.save(self.cuarta_seccion_tarjeta_1_imagen.path,quality=20,optimize=True)
       cuarta_seccion_tarjeta_2_imagen = Image.open(self.cuarta_seccion_tarjeta_2_imagen.path)
       cuarta_seccion_tarjeta_2_imagen.save(self.cuarta_seccion_tarjeta_2_imagen.path,quality=20,optimize=True)
    
    
    def titulo_destacado(self, seccion):
        return self.__dict__[f'{seccion}_seccion_titulo'].replace(self.__dict__[f'{seccion}_seccion_destacado'], f'<strong class="fw-bold text-primary">{self.__dict__[f"{seccion}_seccion_destacado"]}</strong>')

# Banner -> HomeBanner
class Banner(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='carousel', null=True, blank=True)

    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='carousel', verbose_name='imagen', null=True, blank=True)
    subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)

    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    titulo_corto = models.CharField(max_length=255, verbose_name='título corto', null=True, blank=True)
    descripcion_corta = models.CharField(max_length=255, verbose_name='descripción corta', null=True, blank=True)

    
    
    
    def save(self, *args, **kwargs):
       super(Banner, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
    

# Option -> HomeOption
class Opcion(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='opciones', null=True, blank=True)

    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='opciones', verbose_name='imagen', null=True, blank=True)

    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    class Meta:
        verbose_name = 'opción'
        verbose_name_plural = 'opciones'

    
    
    def save(self, *args, **kwargs):
       super(Opcion, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)

# SOMOS STARKEN

class About(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='about', verbose_name='imagen', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    quinta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    quinta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='about', verbose_name='imagen', null=True, blank=True)
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    quinta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    quinta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    class Meta:
        verbose_name = 'somos STARKEN'
        verbose_name_plural = 'somos STARKEN'
    
    
    
    
    def save(self, *args, **kwargs):
       super(About, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       quinta_seccion_imagen = Image.open(self.quinta_seccion_imagen.path)
       quinta_seccion_imagen.save(self.quinta_seccion_imagen.path,quality=20,optimize=True)
    

# Agregar más campos en base a https://desa.sbmundo.com/starken/responsabilidad-social.html
# TODO revisar campos de artículos


class Articulo(BaseModel):
    class Tipo(models.TextChoices):
        NOTICIA = 'noticia', 'Noticia'
        RESPONSABILIDAD_SOCIAL = 'responsabilidad social', 'Responsabilidad social'
        SUSTENTABILIDAD = 'sustentabilidad', 'Sustentabilidad'
    
    tipo = models.CharField(max_length=255, choices=Tipo.choices, verbose_name='tipo', null=True, blank=True)
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
    segunda_seccion_url_primer_boton = models.URLField(verbose_name='url del primer botón', null=True, blank=True)
    segunda_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segunda_seccion_url_segundo_boton = models.URLField(verbose_name='url del segundo botón', null=True, blank=True)
    

    class Meta:
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
    
    
    
    def save(self, *args, **kwargs):
       super(Articulo, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       segunda_seccion_imagen = Image.open(self.segunda_seccion_imagen.path)
       segunda_seccion_imagen.save(self.segunda_seccion_imagen.path,quality=20,optimize=True)
    
        
        
# Starken PRO
class StarkenPro(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    primera_seccion_mensaje = models.CharField(max_length=255, verbose_name='mensaje', null=True, blank=True)

    formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(verbose_name='descripción de formulario', null=True, blank=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='etiqueta mensaje', null=True, blank=True)

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)

    class Meta:
        verbose_name = 'starken PRO'
        verbose_name_plural = 'starken PRO'
    
    
    
    
    def save(self, *args, **kwargs):
       super(StarkenPro, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
    

class StarkenProBeneficio(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    
    
    
    def save(self, *args, **kwargs):
       super(StarkenProBeneficio, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
    

class StarkenProPaso(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    class Meta:
        verbose_name = 'indicaciones'
        verbose_name_plural = 'indicaciones'
    
    
    
#Preguntas Frecuentes
class PreguntasCategoria(models.Model):
    titulo_categoria = models.CharField(max_length=255, verbose_name='Título de categoría', null=True, blank=True)
    
    class Meta:
        verbose_name = 'FAQ - Categoría'
        verbose_name_plural = 'FAQ - Categoría'
    
    
class Preguntas(models.Model):
    pregunta = models.ForeignKey(PreguntasCategoria, on_delete=models.CASCADE, related_name='preguntas',  verbose_name='Preguntas', null=True, blank=True)
    pregunta_titulo = models.CharField(max_length=255, verbose_name='pregunta título', null=True, blank=True)
    pregunta_descripcion = models.TextField(verbose_name='pregunta descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    

class PreguntasFrecuentes(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_boton_buscar = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    
    segunda_seccion_preguntas = models.ManyToManyField(Preguntas, verbose_name='Preguntas', blank=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    tercera_seccion_titulo_primer_bloque = models.CharField(max_length=255, verbose_name='título primer bloque', null=True, blank=True)
    tercera_seccion_descripcion_primer_bloque = models.TextField(verbose_name='descripción primer bloque', null=True, blank=True)
    
    tercera_seccion_titulo_segundo_bloque = models.CharField(max_length=255, verbose_name='título segundo bloque', null=True, blank=True)
    tercera_seccion_descripcion_segundo_bloque = models.TextField(verbose_name='descripción segundo bloque', null=True, blank=True)
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
    
    def __str__(self):
        return self.primera_seccion_titulo
    

    
    
#Help Center
class CentrodeAyuda(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    formulario_titulo_contacto = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion_contacto = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal_contacto = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_nombre_contacto = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email_contacto = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_telefono_contacto = models.CharField(max_length=255, verbose_name='etiqueta phone', null=True, blank=True)
    etiqueta_tipo_de_negocio_contacto = models.CharField(max_length=255, verbose_name='etiqueta tipo de negocio', null=True, blank=True)
    etiqueta_mensaje_contacto = models.CharField(max_length=255, verbose_name='etiqueta mensaje', null=True, blank=True)
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    tercera_seccion_preguntas = models.ManyToManyField(PreguntasCategoria, verbose_name='Preguntas', blank=True)
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='email', null=True, blank=True)
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='mensaje', null=True, blank=True)
    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='CentrodeAyuda', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'centro de ayuda'
        verbose_name_plural = 'centros de ayuda'
    
    
    def save(self, *args, **kwargs):
       super(CentrodeAyuda, self).save(*args, **kwargs)
       cuarta_seccion_imagen = Image.open(self.cuarta_seccion_imagen.path)
       cuarta_seccion_imagen.save(self.cuarta_seccion_imagen.path,quality=20,optimize=True)
    
    
class CentrodeAyudaBeneficio(BaseModel):
    centro_de_ayuda = models.ForeignKey(CentrodeAyuda, on_delete=models.CASCADE, verbose_name='Centro de Ayuda', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    image = models.ImageField(upload_to='centro_de_ayuda', verbose_name='imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    
    
    def save(self, *args, **kwargs):
       super(CentrodeAyudaBeneficio, self).save(*args, **kwargs)
       image = Image.open(self.image.path)
       image.save(self.image.path,quality=20,optimize=True)
    

#Condiciones de Servicio
class TerminosdeServicio(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Condición de Servicio'
        verbose_name_plural = 'Condiciones de Servicio'
class TerminosdeServicioSeccion(models.Model):
    terminos_de_servicio = models.ForeignKey(TerminosdeServicio, on_delete=models.CASCADE, verbose_name='Términos de Servicio', null=True, blank=True)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='id')
    seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Nueva Sección'
        verbose_name_plural = 'Nueva Sección'
    
class TerminosdeServicioPunto(models.Model):
    terminos_de_servicio = models.ForeignKey(TerminosdeServicio, on_delete=models.CASCADE, verbose_name='Términos de Servicio', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título de término', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción de término', null=True, blank=True)
    class Meta:
        verbose_name = 'Punto de Condición de Servicio'
        verbose_name_plural = 'Puntos de Condiciones de Servicio'
        
#Contactanos
class Contactanos(BaseModel):
    formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(verbose_name='descripción de formulario', null=True, blank=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='etiqueta mensaje', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='contactanos', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario', null=True, blank=True)
    tercera_seccion_formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario', null=True, blank=True)
    tercera_seccion_etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    tercera_seccion_etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    tercera_seccion_etiqueta_comentario = models.CharField(max_length=255, verbose_name='etiqueta comentario', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Contáctanos'
        verbose_name_plural = 'Contáctanos'
    
    def save(self, *args, **kwargs):
       super(Contactanos, self).save(*args, **kwargs)
       tercera_seccion_imagen = Image.open(self.tercera_seccion_imagen.path)
       tercera_seccion_imagen.save(self.tercera_seccion_imagen.path,quality=20,optimize=True)
       
    
        
class Datos(models.Model):
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='datos', verbose_name='imagen', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_descripcion = models.CharField(max_length=255, verbose_name='primera descripción', null=True, blank=True)
    segunda_descripcion = models.CharField(max_length=255, verbose_name='segunda descripción', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Contáctanos Datos'
        verbose_name_plural = 'Contáctanos Datos'
    
    def save(self, *args, **kwargs):
       super(Datos, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
        

class Iconos(models.Model):
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto', null=True, blank=True)
    titulo_icono = models.CharField(max_length=255, verbose_name='título ícono', null=True, blank=True)
    alt_icono = models.CharField(max_length=255, verbose_name='alt ícono', null=True, blank=True)
    icono = models.ImageField(upload_to='iconos', verbose_name='ícono', null=True, blank=True)

    class Meta:
        verbose_name = 'Íconos'
        verbose_name_plural = 'Íconos'
    
    def save(self, *args, **kwargs):
       super(Iconos, self).save(*args, **kwargs)
       icono = Image.open(self.icono.path)
       
       size_icono= os.path.getsize(self.icono.path)

       #Calcular la cantidad de peso en la imagen en kbytes
       #Calcular la cantidad de porcentaje segun el peso actual de la imagen y el ideal 200 kbytes
       icono.save(self.icono.path,quality=20,optimize=True)
       
       
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
    segunda_seccion_advertencia = models.CharField(max_length=255, verbose_name='advertencia', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Cotizador'
        verbose_name_plural = 'Cotizadores'
        
class Boton(models.Model):
    cotizador = models.ForeignKey(Cotizador, on_delete=models.CASCADE, verbose_name='Cotizador', null=True, blank=True)
    etiqueta_boton = models.CharField(max_length=255, verbose_name='etiqueta botón', null=True, blank=True)
    destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Botón'
        verbose_name_plural = 'Botones'
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
    primera_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='dhl', verbose_name='imagen de fondo', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    

    tercera_seccion_contenido = RichTextUploadingField(verbose_name='contenido', null=True, blank=True)
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    
    class Meta:
        verbose_name = 'DHL'
        verbose_name_plural = 'DHL'
        
    def save(self, *args, **kwargs):
       super(DHL, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       

class Modalidades(models.Model):
    modalidad = models.ForeignKey(DHL, on_delete=models.CASCADE, verbose_name='Modalidad', null=True, blank=True)
    imagen = models.ImageField(upload_to='dhl', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Modalidades de Servicio'
        verbose_name_plural = 'Modalidades de Servicio'
        
    def save(self, *args, **kwargs):
       super(Modalidades, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       
class Accion(models.Model):
    accion = models.ForeignKey(DHL, on_delete=models.CASCADE, verbose_name='Acción', null=True, blank=True)
    imagen = models.ImageField(upload_to='dhl', verbose_name='imagen', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Acciones'
        verbose_name_plural = 'Acciones'
        
    def save(self, *args, **kwargs):
       super(Accion, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       
       
#Empresas
class Empresas(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='imagen de fondo', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_imagen_fondo = models.ImageField(upload_to='empresas', verbose_name='imagen de fondo', null=True, blank=True)
    formulario_titulo = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_telefono = models.CharField(max_length=255, verbose_name='etiqueta número telefónico', null=True, blank=True)
    etiqueta_tipo_de_negocio = models.CharField(max_length=255, verbose_name='etiqueta tipo de negocio', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='logo', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    tercera_seccion_enlace = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    tercera_seccion_enlace_url = models.URLField(verbose_name='url del enlace', null=True, blank=True)
    
    cuarta_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_titulo_interno = models.CharField(max_length=255, verbose_name='título interno', null=True, blank=True)
    cuarta_seccion_subtitulo_interno = models.CharField(max_length=255, verbose_name='subtítulo interno', null=True, blank=True)
    cuarta_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    cuarta_seccion_primer_boton_url = models.URLField(verbose_name='url del primer botón', null=True, blank=True)
    cuarta_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    cuarta_seccion_segundo_boton_url = models.URLField(verbose_name='url del segundo botón', null=True, blank=True)
    
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    quinta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        
    def save(self, *args, **kwargs):
       super(Empresas, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       tercera_seccion_imagen = Image.open(self.tercera_seccion_imagen.path)
       tercera_seccion_imagen.save(self.tercera_seccion_imagen.path,quality=20,optimize=True)
       tercera_seccion_imagen_fondo = Image.open(self.tercera_seccion_imagen_fondo.path)
       tercera_seccion_imagen_fondo.save(self.tercera_seccion_imagen_fondo.path,quality=20,optimize=True)
       cuarta_seccion_imagen = Image.open(self.cuarta_seccion_imagen.path)
       cuarta_seccion_imagen.save(self.cuarta_seccion_imagen.path,quality=20,optimize=True)
       quinta_seccion_imagen = Image.open(self.quinta_seccion_imagen.path)
       quinta_seccion_imagen.save(self.quinta_seccion_imagen.path,quality=20,optimize=True)
       
class EmpresasBeneficios(models.Model):
    beneficio = models.ForeignKey(Empresas, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    imagen = models.ImageField(upload_to='empresas', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
        
    def save(self, *args, **kwargs):
       super(EmpresasBeneficios, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       

class EmpresasCarrusel(models.Model):
    beneficio = models.ForeignKey(Empresas, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    imagen = models.ImageField(upload_to='empresas', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Imágenes'
        verbose_name_plural = 'Imágenes'
        
    def save(self, *args, **kwargs):
       super(EmpresasCarrusel, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       


#Envíos internacionales
class EnviosInternacionales(BaseModel):
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='envios internacionales', verbose_name='imagen de fondo', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_imagen_primer_bloque = models.ImageField(upload_to='envios internacionales', verbose_name='imagen de fondo primer bloque', null=True, blank=True)
    tercera_seccion_titulo_primer_bloque = models.CharField(max_length=255, verbose_name='título primer bloque', null=True, blank=True)
    tercera_seccion_descripcion_primer_bloque = models.TextField(blank=True, verbose_name='descripción primer bloque', null=True)
    tercera_seccion_boton_primer_bloque = models.CharField(max_length=255, verbose_name='botón primer bloque', null=True, blank=True)
    tercera_seccion_boton_url_primer_bloque = models.URLField(verbose_name='url del botón primer bloque', null=True, blank=True)
    tercera_seccion_imagen_segundo_bloque = models.ImageField(upload_to='envios internacionales', verbose_name='imagen de fondo segundo bloque', null=True, blank=True)
    tercera_seccion_titulo_segundo_bloque = models.CharField(max_length=255, verbose_name='título segundo bloque', null=True, blank=True)
    tercera_seccion_descripcion_segundo_bloque = models.TextField(blank=True, verbose_name='descripción segundo bloque', null=True)
    tercera_seccion_boton_segundo_bloque = models.CharField(max_length=255, verbose_name='botón segundo bloque', null=True, blank=True)
    tercera_seccion_boton_url_segundo_bloque = models.URLField(verbose_name='url del botón segundo bloque', null=True, blank=True)
    
    cuarta_seccion_imagen = models.ImageField(upload_to='envios internacionales', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    quinta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='envios internacionales', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Envíos Internacionales'
        verbose_name_plural = 'Envíos Internacionales'
        
    def save(self, *args, **kwargs):
       super(EnviosInternacionales, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       tercera_seccion_imagen_primer_bloque = Image.open(self.tercera_seccion_imagen_primer_bloque.path)
       tercera_seccion_imagen_primer_bloque.save(self.tercera_seccion_imagen_primer_bloque.path,quality=20,optimize=True)
       tercera_seccion_imagen_segundo_bloque = Image.open(self.tercera_seccion_imagen_segundo_bloque.path)
       tercera_seccion_imagen_segundo_bloque.save(self.tercera_seccion_imagen_segundo_bloque.path,quality=20,optimize=True)
       cuarta_seccion_imagen = Image.open(self.cuarta_seccion_imagen.path)
       cuarta_seccion_imagen.save(self.cuarta_seccion_imagen.path,quality=20,optimize=True)
       quinta_seccion_imagen = Image.open(self.quinta_seccion_imagen.path)
       quinta_seccion_imagen.save(self.quinta_seccion_imagen.path,quality=20,optimize=True)
       
class EnviosInternacionalesBeneficios(models.Model):
    beneficio = models.ForeignKey(EnviosInternacionales, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios internacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
        
    def save(self, *args, **kwargs):
       super(EnviosInternacionalesBeneficios, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       



#Envíos Nacionales
class EnviosNacionales(BaseModel):
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen de fondo', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    
    cuarta_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Envíos Nacionales'
        verbose_name_plural = 'Envíos Nacionales'
        
    def save(self, *args, **kwargs):
       super(EnviosNacionales, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       tercera_seccion_imagen = Image.open(self.tercera_seccion_imagen.path)
       tercera_seccion_imagen.save(self.tercera_seccion_imagen.path,quality=20,optimize=True)
       cuarta_seccion_imagen = Image.open(self.cuarta_seccion_imagen.path)
       cuarta_seccion_imagen.save(self.cuarta_seccion_imagen.path,quality=20,optimize=True)
       
class EnviosNacionalesBeneficios(models.Model):
    beneficio = models.ForeignKey(EnviosNacionales, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios nacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
        
    def save(self, *args, **kwargs):
       super(EnviosNacionalesBeneficios, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       

class EnviosNacionalesRecomendaciones(models.Model):
    recomendacion = models.ForeignKey(EnviosNacionales, on_delete=models.CASCADE, verbose_name='Recomendaciones', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios nacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    url = models.URLField(verbose_name='url', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Recomendaciones'
        verbose_name_plural = 'Recomendaciones'
        
    def save(self, *args, **kwargs):
       super(EnviosNacionalesRecomendaciones, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       


#Mi Primer Envío
class MiPrimerEnvio(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen de fondo', null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Mi Primer Envío'
        verbose_name_plural = 'Mi Primer Envío'
        
    def save(self, *args, **kwargs):
       super(MiPrimerEnvio, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       
class MiPrimerEnvioStep(models.Model):
    beneficio = models.ForeignKey(MiPrimerEnvio, on_delete=models.CASCADE, verbose_name='Step', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios nacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = RichTextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Indicaciones'
        verbose_name_plural = 'Indicaciones'
        
    def save(self, *args, **kwargs):
       super(MiPrimerEnvioStep, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)


#Mypymes
class Mypymes(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_video = models.URLField(verbose_name='video', null=True, blank=True)
    primera_seccion_miniatura = models.ImageField(upload_to='mypymes', verbose_name='imagen miniatura', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    
    tercera_seccion_imagen_fondo = models.ImageField(upload_to='mypymes', verbose_name='imagen de fondo', null=True, blank=True)
    formulario_titulo = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_telefono = models.CharField(max_length=255, verbose_name='etiqueta número telefónico', null=True, blank=True)
    etiqueta_tipo_de_negocio = models.CharField(max_length=255, verbose_name='etiqueta tipo de negocio', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='logo', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    tercera_seccion_enlace = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    tercera_seccion_enlace_url = models.URLField(verbose_name='url del enlace', null=True, blank=True)
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    
    sexta_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    sexta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    sexta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    sexta_seccion_titulo_interno = models.CharField(max_length=255, verbose_name='título interno', null=True, blank=True)
    sexta_seccion_subtitulo_interno = models.CharField(max_length=255, verbose_name='subtítulo interno', null=True, blank=True)
    sexta_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    sexta_seccion_primer_boton_url = models.URLField(verbose_name='url del primer botón', null=True, blank=True)
    sexta_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    sexta_seccion_segundo_boton_url = models.URLField(verbose_name='url del segundo botón', null=True, blank=True)
    
    septima_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    septima_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    septima_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    septima_seccion_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)
    septima_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'MYPYMES'
        verbose_name_plural = 'MYPYMES'
        
    def save(self, *args, **kwargs):
       super(Mypymes, self).save(*args, **kwargs)
       primera_seccion_imagen = Image.open(self.primera_seccion_imagen.path)
       primera_seccion_imagen.save(self.primera_seccion_imagen.path,quality=20,optimize=True)
       primera_seccion_miniatura = Image.open(self.primera_seccion_miniatura.path)
       primera_seccion_miniatura.save(self.primera_seccion_miniatura.path,quality=20,optimize=True)
       tercera_seccion_imagen = Image.open(self.tercera_seccion_imagen.path)
       tercera_seccion_imagen.save(self.tercera_seccion_imagen.path,quality=20,optimize=True)
       tercera_seccion_imagen_fondo = Image.open(self.tercera_seccion_imagen_fondo.path)
       tercera_seccion_imagen_fondo.save(self.tercera_seccion_imagen_fondo.path,quality=20,optimize=True)
       sexta_seccion_imagen = Image.open(self.sexta_seccion_imagen.path)
       sexta_seccion_imagen.save(self.sexta_seccion_imagen.path,quality=20,optimize=True)
       septima_seccion_imagen = Image.open(self.septima_seccion_imagen.path)
       septima_seccion_imagen.save(self.septima_seccion_imagen.path,quality=20,optimize=True)
       
class MypymesBeneficios(models.Model):
    beneficio = models.ForeignKey(Mypymes, on_delete=models.CASCADE, verbose_name='Beneficio', null=True, blank=True)
    imagen = models.ImageField(upload_to='mypymes', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
        
    def save(self, *args, **kwargs):
       super(MypymesBeneficios, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)
       
class MypymesIndicaciones(models.Model):
    mypymes = models.ForeignKey(Mypymes, on_delete=models.CASCADE, verbose_name='Mypymes', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    class Meta:
        verbose_name = 'indicaciones'
        verbose_name_plural = 'indicaciones'
        

class MypymesTestimonios(models.Model):
    mypymes = models.ForeignKey(Mypymes, on_delete=models.CASCADE, verbose_name='Mypymes', null=True, blank=True)
    testimonio = models.TextField(verbose_name='testimonio', null=True, blank=True)
    nombre = models.CharField(max_length=255, verbose_name='Nombre', null=True, blank=True)
    apellido = models.CharField(max_length=255, verbose_name='Apellido', null=True, blank=True)
    puesto_laboral = models.CharField(max_length=255, verbose_name='Puesto Laboral', null=True, blank=True)
    imagen = models.ImageField(upload_to='mypymes', verbose_name='Imagen de Perfil', null=True, blank=True)
    class Meta:
        verbose_name = 'Testimonios'
        verbose_name_plural = 'Testimonios'
    
    def save(self, *args, **kwargs):
       super(MypymesTestimonios, self).save(*args, **kwargs)
       imagen = Image.open(self.imagen.path)
       imagen.save(self.imagen.path,quality=20,optimize=True)