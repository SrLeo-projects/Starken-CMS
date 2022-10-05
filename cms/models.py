from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    class Meta:
        abstract = True

class Servicio(BaseModel):
    imagen = models.ImageField(upload_to='servicios', verbose_name='imagen', null=True, blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    class Meta:
        verbose_name = 'servicio'

class Home(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón principal', null=True, blank=True)
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón principal', null=True, blank=True)

    primera_seccion_boton_secundario = models.CharField(max_length=255, verbose_name='botón secundario', null=True, blank=True)
    primera_seccion_boton_secundario_url = models.URLField(verbose_name='url del botón secundario', null=True, blank=True)

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

    cuarta_seccion_tarjeta_1_imagen = models.ImageField(upload_to='home', verbose_name='imagen', null=True, blank=True)
    cuarta_seccion_tarjeta_1_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    cuarta_seccion_tarjeta_1_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    cuarta_seccion_tarjeta_1_boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

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
    
    def __str__(self):
        return self.titulo
    
    def titulo_destacado(self, seccion):
        return self.__dict__[f'{seccion}_seccion_titulo'].replace(self.__dict__[f'{seccion}_seccion_destacado'], f'<strong class="fw-bold text-primary">{self.__dict__[f"{seccion}_seccion_destacado"]}</strong>')

# Banner -> HomeBanner
class Banner(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='carousel', null=True, blank=True)

    imagen = models.ImageField(upload_to='carousel', verbose_name='imagen', null=True, blank=True)
    subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', null=True, blank=True)

    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    titulo_corto = models.CharField(max_length=255, verbose_name='título corto', null=True, blank=True)
    descripcion_corta = models.CharField(max_length=255, verbose_name='descripción corta', null=True, blank=True)

    def __str__(self):
        return self.titulo

# Option -> HomeOption
class Opcion(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='opciones', null=True, blank=True)

    imagen = models.ImageField(upload_to='opciones', verbose_name='imagen', null=True, blank=True)

    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.URLField(verbose_name='url del botón', null=True, blank=True)

    class Meta:
        verbose_name = 'opción'
        verbose_name_plural = 'opciones'

    def __str__(self):
        return self.titulo

# SOMOS STARKEN

class About(BaseModel):
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
    
    def __str__(self):
        return self.titulo

# Agregar más campos en base a https://desa.sbmundo.com/starken/responsabilidad-social.html
# TODO revisar campos de artículos
class RedesSociales(models.Model):
    imagen = models.ImageField(upload_to='articles', verbose_name='imagen', null=True, blank=True)
    url = models.URLField(verbose_name='url', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Artículos Redes Sociales'
        verbose_name_plural = 'Artículos Redes Sociales'

class Articulo(BaseModel):
    class Tipo(models.TextChoices):
        NOTICIA = 'noticia', 'Noticia'
        RESPONSABILIDAD_SOCIAL = 'responsabilidad social', 'Responsabilidad social'
        SUSTENTABILIDAD = 'sustentabilidad', 'Sustentabilidad'
    primera_seccion_logo = models.ImageField(upload_to='logos', verbose_name='logo', null=True, blank=True)
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    tipo = models.CharField(max_length=255, choices=Tipo.choices, verbose_name='tipo', null=True, blank=True)
    segunda_seccion_etiqueta = models.CharField(max_length=255, verbose_name='etiqueta', null=True, blank=True)
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    segunda_seccion_fecha_de_creacion = models.DateField(verbose_name='fecha de creación', null=True, blank=True)
    segunda_seccion_imagen = models.ImageField(upload_to='articles', verbose_name='imagen', null=True, blank=True)
    segunda_seccion_contenido = RichTextUploadingField(verbose_name='contenido', null=True, blank=True)
    redes_sociales = models.ManyToManyField(RedesSociales, verbose_name='Redes Sociales', blank=True)
    fecha_de_actualizacion = models.DateField(verbose_name='fecha de actualización', null=True, blank=True)
    
    tercera_seccion_imagen = models.ImageField(upload_to='articles', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    tercera_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    tercera_seccion_url_primer_boton = models.URLField(verbose_name='url del primer botón', null=True, blank=True)
    tercera_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    tercera_seccion_url_segundo_boton = models.URLField(verbose_name='url del segundo botón', null=True, blank=True)
    

    class Meta:
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
    
    def __str__(self):
        return self.titulo
    
class ContenidoArticulo(BaseModel):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name='Artículo', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    imagen = models.ImageField(upload_to='articles', verbose_name='imagen', null=True, blank=True)
    contenido = models.TextField(verbose_name='contenido', null=True, blank=True)
    fecha_de_creacion = models.DateField(verbose_name='fecha de creación', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Contenido de Artículo'
        verbose_name_plural = 'Contenido de Artículo'
        
        
# Starken PRO
class StarkenPro(BaseModel):
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
    
    def __str__(self):
        return self.titulo

class StarkenProBeneficio(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)
    imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    def __str__(self):
        return self.titulo

class StarkenProPaso(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO', null=True, blank=True)

    class Meta:
        verbose_name = 'paso'
        verbose_name_plural = 'pasos'
    
    def __str__(self):
        return self.titulo
    
#Preguntas Frecuentes
class PreguntasFrecuentes(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_seccion_boton_buscar = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    segunda_seccion_descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    
    segunda_seccion_titulo_primer_bloque = models.CharField(max_length=255, verbose_name='título primer bloque', null=True, blank=True)
    segunda_seccion_descripcion_primer_bloque = models.TextField(verbose_name='descripción primer bloque', null=True, blank=True)
    
    segunda_seccion_titulo_segundo_bloque = models.CharField(max_length=255, verbose_name='título segundo bloque', null=True, blank=True)
    segunda_seccion_descripcion_segundo_bloque = models.TextField(verbose_name='descripción segundo bloque', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Pregunta Frecuente'
        verbose_name_plural = 'Preguntas Frecuentes'
    
    def __str__(self):
        return self.primera_seccion_titulo
    
class PreguntasCategoria(BaseModel):
    categoria = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, verbose_name='Categoría de Preguntas', null=True, blank=True)
    titulo_categoria = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Preguntas categoría'
        verbose_name_plural = 'Preguntas categoría'
    
    def __str__(self):
        return self.titulo_categoria
    
class Preguntas(models.Model):
    pregunta = models.ForeignKey(PreguntasCategoria, on_delete=models.CASCADE, verbose_name='Preguntas', null=True, blank=True)
    pregunta_titulo = models.CharField(max_length=255, verbose_name='pregunta título', null=True, blank=True)
    pregunta_descripcion = models.TextField(verbose_name='pregunta descripción', null=True, blank=True)
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    
    def __str__(self):
        return self.titulo_categoria
    
    
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
    
    formulario_titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción', null=True)
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='nombre', null=True, blank=True)
    etiqueta_email = models.CharField(max_length=255, verbose_name='email', null=True, blank=True)
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='mensaje', null=True, blank=True)
    cuarta_seccion_imagen = models.ImageField(upload_to='CentrodeAyuda', verbose_name='imagen', null=True, blank=True)
    
    class Meta:
        verbose_name = 'centro de ayuda'
        verbose_name_plural = 'centros de ayuda'
        
class CentrodeAyudaPregunta(BaseModel):
    centro_de_ayuda = models.ForeignKey(CentrodeAyuda, on_delete=models.CASCADE, verbose_name='Centro de Ayuda', null=True, blank=True)
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    
class CentrodeAyudaBeneficio(BaseModel):
    centro_de_ayuda = models.ForeignKey(CentrodeAyuda, on_delete=models.CASCADE, verbose_name='Centro de Ayuda', null=True, blank=True)
    image = models.ImageField(upload_to='centro_de_ayuda', verbose_name='imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    def __str__(self):
        return self.titulo

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
    
    tercera_seccion_imagen = models.ImageField(upload_to='contactanos', verbose_name='imagen', null=True, blank=True)
    tercera_seccion_formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario', null=True, blank=True)
    tercera_seccion_formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario', null=True, blank=True)
    tercera_seccion_etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre', null=True, blank=True)
    tercera_seccion_etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email', null=True, blank=True)
    tercera_seccion_etiqueta_comentario = models.CharField(max_length=255, verbose_name='etiqueta comentario', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Contáctanos'
        verbose_name_plural = 'Contáctanos'
        
class Datos(models.Model):
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto', null=True, blank=True)
    imagen = models.ImageField(upload_to='datos', verbose_name='imagen', null=True, blank=True)
    titulo = models.CharField(max_length=255, verbose_name='título', null=True, blank=True)
    primera_descripcion = models.TextField(verbose_name='primera descripción', null=True, blank=True)
    segunda_descripcion = models.TextField(verbose_name='segunda descripción', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Contáctanos Datos'
        verbose_name_plural = 'Contáctanos Datos'

class Iconos(models.Model):
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto', null=True, blank=True)
    icono = models.ImageField(upload_to='iconos', verbose_name='imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'Íconos'
        verbose_name_plural = 'Íconos'