from enum import unique
import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


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
        return Tipo(self.status).color_class()
    
    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
    
    
    
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
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True) 
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
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    segunda_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    segunda_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='segunda_url_boton_principal', null=True, blank=True)

    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='seguimiento', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    tercera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='tercera_url_boton_principal', null=True, blank=True)

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
    quinta_seccion_imagen = models.ImageField(upload_to='seguimiento', verbose_name='imagen', null=True, blank=True)
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_palabras = models.CharField(max_length=255, verbose_name='palabras', help_text='separadas por coma', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    quinta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='quinta_url_boton_principal', null=True, blank=True)

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

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    tercera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='tercera_url_boton_principal_about', null=True, blank=True)
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='cuarta_url_boton_principal_about', null=True, blank=True)

    quinta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    quinta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    quinta_seccion_imagen = models.ImageField(upload_to='about', verbose_name='imagen', null=True, blank=True)
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    quinta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    quinta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    quinta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    quinta_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='quinta_url_boton_principal_about', null=True, blank=True)
    
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
    slug = models.SlugField(null=True, blank=True, unique=True) 
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
    
    

    
        
        
# Starken PRO
class StarkenPro(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='url_boton_principal_starkenpro', null=True, blank=True)
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
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")

    class Meta:
        verbose_name = 'starken PRO'
        verbose_name_plural = 'starken PRO'

    

class StarkenProBeneficio(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    

    

class StarkenProPaso(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)
    paso = models.CharField(max_length=255, verbose_name='número de indicación', null=True, blank=True)
    imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    class Meta:
        verbose_name = 'indicaciones'
        verbose_name_plural = 'indicaciones'
        
    
#Preguntas Frecuentes
class PreguntasCategoria(models.Model):
    titulo_categoria = models.CharField(max_length=255, verbose_name='Título de categoría', null=True, blank=True)
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'FAQ - Categoría'
        verbose_name_plural = 'FAQ - Categoría'
        
    def __str__(self):
            return self.titulo_categoria
    
    
class Preguntas(models.Model):
    pregunta = models.ForeignKey(PreguntasCategoria, on_delete=models.CASCADE, related_name='preguntas',  verbose_name='Preguntas', null=True, blank=True)
    pregunta_titulo = models.CharField(max_length=255, verbose_name='pregunta título', null=True, blank=True)
    pregunta_descripcion = models.TextField(verbose_name='pregunta descripción', null=True, blank=True)
    
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
    
    tercera_seccion_titulo_primer_bloque = models.CharField(max_length=255, verbose_name='título primer bloque', null=True, blank=True)
    tercera_seccion_descripcion_primer_bloque = models.TextField(verbose_name='descripción primer bloque', null=True, blank=True)
    
    tercera_seccion_titulo_segundo_bloque = models.CharField(max_length=255, verbose_name='título segundo bloque', null=True, blank=True)
    tercera_seccion_descripcion_segundo_bloque = models.TextField(verbose_name='descripción segundo bloque', null=True, blank=True)
    
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
    
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    segunda_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    segunda_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='segunda_url_boton_principal_centro_de_ayuda', null=True, blank=True)
    segunda_seccion_preguntas = models.ManyToManyField(Preguntas, verbose_name='Preguntas', blank=True)
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='email', null=True, blank=True)
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
    url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='URL', related_name='url_centro_de_ayuda_beneficio', null=True, blank=True)
    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    

#Condiciones de Servicio
class TerminosdeServicio(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
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
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='dhl', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
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
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    tercera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Contáctanos'
        verbose_name_plural = 'Contáctanos'
    
        
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

class Iconos(models.Model):
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto', null=True, blank=True)
    titulo_icono = models.CharField(max_length=255, verbose_name='título ícono', null=True, blank=True)
    alt_icono = models.CharField(max_length=255, verbose_name='alt ícono', null=True, blank=True)
    icono = models.ImageField(upload_to='iconos', verbose_name='ícono', null=True, blank=True)

    class Meta:
        verbose_name = 'Íconos'
        verbose_name_plural = 'Íconos'
 
       
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
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    segunda_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Cotizador'
        verbose_name_plural = 'Cotizador'
        
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
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_principal_dhl', null=True, blank=True)
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='dhl', verbose_name='imagen de fondo', null=True, blank=True)
    primera_seccion_titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    primera_seccion_alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    primera_seccion_imagen_movil = models.ImageField(upload_to='carousel', verbose_name='imagen móvil', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    segunda_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    

    tercera_seccion_contenido = RichTextUploadingField(verbose_name='contenido', null=True, blank=True)
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='cuarta_url_boton_principal_dhl', null=True, blank=True)
    
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
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
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
    formulario_titulo = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_telefono = models.CharField(max_length=255, verbose_name='etiqueta número telefónico', null=True, blank=True)
    etiqueta_tipo_de_negocio = models.CharField(max_length=255, verbose_name='etiqueta tipo de negocio', null=True, blank=True)
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='logo', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    tercera_seccion_enlace = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    tercera_seccion_enlace_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del enlace', related_name='url_enlace_empresas', null=True, blank=True)
    
    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='empresas', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_titulo_interno = models.CharField(max_length=255, verbose_name='título interno', null=True, blank=True)
    cuarta_seccion_subtitulo_interno = models.CharField(max_length=255, verbose_name='subtítulo interno', null=True, blank=True)
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
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
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
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
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
    
    cuarta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    cuarta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='envios nacionales', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    cuarta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    cuarta_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='cuarta_url_boton_envios_nacionales', null=True, blank=True)
    
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
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
       

class EnviosNacionalesRecomendaciones(models.Model):
    recomendacion = models.ForeignKey(EnviosNacionales, on_delete=models.CASCADE, verbose_name='Recomendaciones', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='envios nacionales', verbose_name='ícono', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
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
    
    class Meta:
        verbose_name = 'Indicaciones'
        verbose_name_plural = 'Indicaciones'


#Mypymes
class Mypymes(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_mypymes', null=True, blank=True)
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
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_telefono = models.CharField(max_length=255, verbose_name='etiqueta número telefónico', null=True, blank=True)
    etiqueta_tipo_de_negocio = models.CharField(max_length=255, verbose_name='etiqueta tipo de negocio', null=True, blank=True)
    tercera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    tercera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    tercera_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='logo', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    tercera_seccion_enlace = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    tercera_seccion_enlace_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del enlace', related_name='url_enlace_mypymes', null=True, blank=True)
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    quinta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    
    sexta_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    sexta_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    sexta_seccion_imagen = models.ImageField(upload_to='mypymes', verbose_name='imagen', null=True, blank=True)
    sexta_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    sexta_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    sexta_seccion_titulo_interno = models.CharField(max_length=255, verbose_name='título interno', null=True, blank=True)
    sexta_seccion_subtitulo_interno = models.CharField(max_length=255, verbose_name='subtítulo interno', null=True, blank=True)
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
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Beneficios'
        verbose_name_plural = 'Beneficios'
       
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
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='mypymes', verbose_name='Imagen de Perfil', null=True, blank=True)
    class Meta:
        verbose_name = 'Testimonios'
        verbose_name_plural = 'Testimonios'
       
       
#Reclamos

class Reclamos(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='reclamos', verbose_name='imagen', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='primera_url_boton_reclamos', null=True, blank=True)
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título formulario', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción formulario', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón formulario', null=True, blank=True)
    etiqueta_rut = models.CharField(max_length=255, verbose_name='etiqueta RUT', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    etiqueta_telefono = models.CharField(max_length=255, verbose_name='etiqueta número telefónico', null=True, blank=True)
    etiqueta_reclamo = models.CharField(max_length=255, verbose_name='etiqueta reclamo', null=True, blank=True)
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='enlace', null=True, blank=True)
    tercera_seccion_enlace_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del enlace', related_name='url_enlace_reclamos', null=True, blank=True)
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
    recomendación_descripcion = models.TextField(verbose_name='recomendación descripción', null=True, blank=True)
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
    cuarta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_boton_principal_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón principal', related_name='url_boton_principal_seguimiento', null=True, blank=True)
    
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
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    class Meta:
        verbose_name = 'Sucursales'
        verbose_name_plural = 'Sucursales'
    
class Covid(BaseModel):
    primera_seccion_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    primera_seccion_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    primera_seccion_imagen = models.ImageField(upload_to='seguimiento', verbose_name='imagen miniatura', null=True, blank=True)
    primera_seccion_video_url = models.URLField(verbose_name='url del video', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_fecha = models.DateField(verbose_name='fecha', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    primera_seccion_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    primera_seccion_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del botón', related_name='url_boton_covid', null=True, blank=True)
    
    primera_seccion_ocultar = models.BooleanField(default=False, verbose_name="Ocultar")
    
    class Meta:
        verbose_name = 'Covid-19'
        verbose_name_plural = 'Covid-19'

       
class CovidComunicado(models.Model):
    covid = models.ForeignKey(Covid, on_delete=models.CASCADE, verbose_name='Covid', null=True, blank=True)
    primera_seccion_fecha = models.DateField(verbose_name='fecha', null=True, blank=True)
    primera_seccion_contenido = RichTextUploadingField(verbose_name='contenido', null=True, blank=True)
    class Meta:
        verbose_name = 'Comunicado'
        verbose_name_plural = 'Comunicados'