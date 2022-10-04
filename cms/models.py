from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='título')
    descripcion = models.TextField(blank=True, verbose_name='descripción')

    class Meta:
        abstract = True

class Servicio(BaseModel):
    imagen = models.ImageField(upload_to='servicios', verbose_name='imagen')
    boton = models.CharField(max_length=255, verbose_name='botón')
    boton_url = models.URLField(verbose_name='url del botón')

    class Meta:
        verbose_name = 'servicio'

class Home(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal')
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón principal')

    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario')
    primera_seccion_boton_secundario_url = models.URLField(verbose_name='url del botón secundario')

    primera_seccion_imagen = models.ImageField(upload_to='home', verbose_name='imagen')
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo')
    primera_seccion_subtitulo_descripcion = models.TextField(blank=True, verbose_name='descripción')

    primera_seccion_link = models.URLField(verbose_name='enlace')
    primera_seccion_link_texto = models.CharField(max_length=255, verbose_name='texto del enlace')

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')

    segunda_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal')
    segunda_seccion_boton_principal_url = models.URLField(verbose_name='url del botón principal')

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')

    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal')
    tercera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón principal')

    cuarta_seccion_tarjeta_1_imagen = models.ImageField(upload_to='home', verbose_name='imagen')
    cuarta_seccion_tarjeta_1_titulo = models.CharField(max_length=255, verbose_name='título')
    cuarta_seccion_tarjeta_1_descripcion = models.TextField(blank=True, verbose_name='descripción')
    cuarta_seccion_tarjeta_1_boton = models.CharField(max_length=255, verbose_name='botón')
    cuarta_seccion_tarjeta_1_boton_url = models.URLField(verbose_name='url del botón')

    cuarta_seccion_tarjeta_2_imagen = models.ImageField(upload_to='home', verbose_name='imagen')
    cuarta_seccion_tarjeta_2_titulo = models.CharField(max_length=255, verbose_name='título')
    cuarta_seccion_tarjeta_2_descripcion = models.TextField(blank=True, verbose_name='descripción')
    cuarta_seccion_tarjeta_2_boton = models.CharField(max_length=255, verbose_name='botón')
    cuarta_seccion_tarjeta_2_boton_url = models.URLField(verbose_name='url del botón')

    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    quinta_seccion_palabras = models.CharField(max_length=255, verbose_name='palabras', help_text='separadas por coma')
    quinta_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')

    quinta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    quinta_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')

    servicios = models.ManyToManyField(Servicio, verbose_name='servicios')

    class Meta:
        verbose_name_plural = 'home'
    
    def __str__(self):
        return self.titulo
    
    def titulo_destacado(self, seccion):
        return self.__dict__[f'{seccion}_seccion_titulo'].replace(self.__dict__[f'{seccion}_seccion_destacado'], f'<strong class="fw-bold text-primary">{self.__dict__[f"{seccion}_seccion_destacado"]}</strong>')

# Banner -> HomeBanner
class Banner(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='carousel')

    imagen = models.ImageField(upload_to='carousel', verbose_name='imagen')
    subtitulo = models.CharField(max_length=255, verbose_name='subtítulo')

    boton = models.CharField(max_length=255, verbose_name='botón')
    boton_url = models.URLField(verbose_name='url del botón')

    titulo_corto = models.CharField(max_length=255, verbose_name='título corto')
    descripcion_corta = models.CharField(max_length=255, verbose_name='descripción corta')

    def __str__(self):
        return self.titulo

# Option -> HomeOption
class Opcion(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='opciones')

    imagen = models.ImageField(upload_to='opciones', verbose_name='imagen')

    boton = models.CharField(max_length=255, verbose_name='botón')
    boton_url = models.URLField(verbose_name='url del botón')

    class Meta:
        verbose_name = 'opción'
        verbose_name_plural = 'opciones'

    def __str__(self):
        return self.titulo

# SOMOS STARKEN

class About(BaseModel):
    primera_seccion_imagen = models.ImageField(upload_to='about', verbose_name='imagen')
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    tercera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')
    
    cuarta_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    cuarta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    cuarta_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    cuarta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    cuarta_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')

    quinta_seccion_imagen = models.ImageField(upload_to='about', verbose_name='imagen')
    quinta_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    quinta_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    quinta_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo')
    quinta_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    quinta_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    quinta_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')

    class Meta:
        verbose_name = 'somos STARKEN'
        verbose_name_plural = 'somos STARKEN'
    
    def __str__(self):
        return self.titulo

# Agregar más campos en base a https://desa.sbmundo.com/starken/responsabilidad-social.html
# TODO revisar campos de artículos
class Articulo(BaseModel):
    class Tipo(models.TextChoices):
        NOTICIA = 'noticia', 'Noticia'
        RESPONSABILIDAD_SOCIAL = 'responsabilidad social', 'Responsabilidad social'
        SUSTENTABILIDAD = 'sustentabilidad', 'Sustentabilidad'

    imagen = models.ImageField(upload_to='articles', verbose_name='imagen')
    titulo = models.CharField(max_length=255, verbose_name='título')
    contenido = RichTextUploadingField(verbose_name='contenido')
    tipo = models.CharField(max_length=255, choices=Tipo.choices, verbose_name='tipo')

    fecha_de_creacion = models.DateField(verbose_name='fecha de creación')
    fecha_de_actualizacion = models.DateField(verbose_name='fecha de actualización')

    class Meta:
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
    
    def __str__(self):
        return self.titulo

# Starken PRO
class StarkenPro(BaseModel):
    primera_seccion_imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen')
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')
    primera_seccion_mensaje = models.CharField(max_length=255, verbose_name='mensaje')

    formulario_titulo = models.CharField(max_length=255, verbose_name='título')
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción')
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='nombre')
    etiqueta_email = models.CharField(max_length=255, verbose_name='email')
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='mensaje')

    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')

    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')

    class Meta:
        verbose_name = 'starken PRO'
        verbose_name_plural = 'starken PRO'
    
    def __str__(self):
        return self.titulo

class StarkenProBeneficio(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO')
    imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen')

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    def __str__(self):
        return self.titulo

class StarkenProPaso(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO')

    class Meta:
        verbose_name = 'paso'
        verbose_name_plural = 'pasos'
    
    def __str__(self):
        return self.titulo
    
#Help Center
class CentrodeAyuda(BaseModel):
    formulario_titulo_contacto = models.CharField(max_length=255, verbose_name='título_contacto')
    formulario_descripcion_contacto = models.TextField(blank=True, verbose_name='descripción_contacto')
    formulario_boton_principal_contacto = models.CharField(max_length=255, verbose_name='botón_contacto')
    etiqueta_nombre_contacto = models.CharField(max_length=255, verbose_name='nombre_contacto')
    etiqueta_email_contacto = models.CharField(max_length=255, verbose_name='email_contacto')
    etiqueta_telefono_contacto = models.CharField(max_length=255, verbose_name='phone_contacto')
    etiqueta_tipo_de_negocio_contacto = models.CharField(max_length=255, verbose_name='tipo_de_negocio_contacto')
    etiqueta_mensaje_contacto = models.CharField(max_length=255, verbose_name='mensaje_contacto')
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    segunda_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    tercera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    tercera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    tercera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título')
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción')
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    etiqueta_name = models.CharField(max_length=255, verbose_name='nombre')
    etiqueta_email = models.CharField(max_length=255, verbose_name='email')
    etiqueta_message = models.CharField(max_length=255, verbose_name='mensaje')
    cuarta_seccion_image = models.ImageField(upload_to='CentrodeAyuda', verbose_name='imagen')
    
    class Meta:
        verbose_name = 'centro de ayuda'
        verbose_name_plural = 'centros de ayuda'
        
class CentrodeAyudaPregunta(BaseModel):
    centro_de_ayuda = models.ForeignKey(CentrodeAyuda, on_delete=models.CASCADE, verbose_name='Centro de Ayuda')
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    
class CentrodeAyudaBeneficio(BaseModel):
    centro_de_ayuda = models.ForeignKey(CentrodeAyuda, on_delete=models.CASCADE, verbose_name='Centro de Ayuda')
    image = models.ImageField(upload_to='centro_de_ayuda', verbose_name='imagen')

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    def __str__(self):
        return self.titulo

#Condiciones de Servicio
class TerminosdeServicio(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    
    class Meta:
        verbose_name = 'Condición de Servicio'
        verbose_name_plural = 'Condiciones de Servicio'

class TerminosdeServicioPunto(models.Model):
    terminos_de_servicio = models.ForeignKey(TerminosdeServicio, on_delete=models.CASCADE, verbose_name='Términos de Servicio')
    class Meta:
        verbose_name = 'Punto de Condición de Servicio'
        verbose_name_plural = 'Puntos de Condiciones de Servicio'