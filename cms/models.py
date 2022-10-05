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
class RedesSociales(models.Model):
    imagen = models.ImageField(upload_to='articles', verbose_name='imagen', default='')
    url = models.URLField(verbose_name='url', default='')
    
    class Meta:
        verbose_name = 'Artículos Redes Sociales'
        verbose_name_plural = 'Artículos Redes Sociales'

class Articulo(BaseModel):
    class Tipo(models.TextChoices):
        NOTICIA = 'noticia', 'Noticia'
        RESPONSABILIDAD_SOCIAL = 'responsabilidad social', 'Responsabilidad social'
        SUSTENTABILIDAD = 'sustentabilidad', 'Sustentabilidad'
    primera_seccion_logo = models.ImageField(upload_to='logos', verbose_name='logo', default='')
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', default='')
    
    tipo = models.CharField(max_length=255, choices=Tipo.choices, verbose_name='tipo')
    segunda_seccion_etiqueta = models.CharField(max_length=255, verbose_name='etiqueta', default='')
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', default='')
    segunda_seccion_fecha_de_creacion = models.DateField(verbose_name='fecha de creación')
    segunda_seccion_imagen = models.ImageField(upload_to='articles', verbose_name='imagen', default='')
    segunda_seccion_contenido = RichTextUploadingField(verbose_name='contenido', default='')
    redes_sociales = models.ManyToManyField(RedesSociales, verbose_name='Redes Sociales', default='')
    fecha_de_actualizacion = models.DateField(verbose_name='fecha de actualización')
    
    tercera_seccion_imagen = models.ImageField(upload_to='articles', verbose_name='imagen', default='')
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    tercera_seccion_primer_boton = models.CharField(max_length=255, verbose_name='primer botón', default='')
    tercera_seccion_url_primer_boton = models.URLField(verbose_name='url del primer botón', default='')
    tercera_seccion_segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', default='')
    tercera_seccion_url_segundo_boton = models.URLField(verbose_name='url del segundo botón', default='')
    

    class Meta:
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
    
    def __str__(self):
        return self.titulo
    
class ContenidoArticulo(BaseModel):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name='Artículo')
    titulo = models.CharField(max_length=255, verbose_name='título', default='')
    imagen = models.ImageField(upload_to='articles', verbose_name='imagen', default='')
    contenido = models.TextField(blank=True, verbose_name='contenido', default='')
    fecha_de_creacion = models.DateField(verbose_name='fecha de creación')
    
    class Meta:
        verbose_name = 'Contenido de Artículo'
        verbose_name_plural = 'Contenido de Artículo'
        
        
# Starken PRO
class StarkenPro(BaseModel):
    primera_seccion_imagen = models.ImageField(upload_to='starkenpro', verbose_name='imagen')
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título')
    primera_seccion_destacado = models.CharField(max_length=255, verbose_name='destacado')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón')
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón')
    primera_seccion_mensaje = models.CharField(max_length=255, verbose_name='mensaje')

    formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario')
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción de formulario')
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario')
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre')
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email')
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='etiqueta mensaje')

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
    
#Preguntas Frecuentes
class PreguntasFrecuentes(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    primera_seccion_boton_buscar = models.CharField(max_length=255, verbose_name='botón', null=True, default='')
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción')
    
    segunda_seccion_titulo_primer_bloque = models.CharField(max_length=255, verbose_name='título primer bloque', default='')
    segunda_seccion_descripcion_primer_bloque = models.TextField(blank=True, verbose_name='descripción primer bloque')
    
    segunda_seccion_titulo_segundo_bloque = models.CharField(max_length=255, verbose_name='título segundo bloque', default='')
    segunda_seccion_descripcion_segundo_bloque = models.TextField(blank=True, verbose_name='descripción segundo bloque')
    
    class Meta:
        verbose_name = 'Pregunta Frecuente'
        verbose_name_plural = 'Preguntas Frecuentes'
    
    def __str__(self):
        return self.primera_seccion_titulo
    
class PreguntasCategoria(BaseModel):
    categoria = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, verbose_name='Categoría de Preguntas')
    titulo_categoria = models.CharField(max_length=255, verbose_name='título', default='')
    
    class Meta:
        verbose_name = 'Preguntas categoría'
        verbose_name_plural = 'Preguntas categoría'
    
    def __str__(self):
        return self.titulo_categoria
    
class Preguntas(models.Model):
    pregunta = models.ForeignKey(PreguntasCategoria, on_delete=models.CASCADE, verbose_name='Preguntas')
    pregunta_titulo = models.CharField(max_length=255, verbose_name='pregunta título', default='')
    pregunta_descripcion = models.TextField(blank=True, verbose_name='pregunta descripción', default='')
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    
    def __str__(self):
        return self.titulo_categoria
    
    
#Help Center
class CentrodeAyuda(BaseModel):
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='titulo')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', default='descripcion')
    primera_seccion_boton_principal = models.CharField(max_length=255, verbose_name='botón', null=True, default='boton')
    primera_seccion_boton_principal_url = models.URLField(verbose_name='url del botón', default='boton')
    formulario_titulo_contacto = models.CharField(max_length=255, verbose_name='título formulario')
    formulario_descripcion_contacto = models.TextField(blank=True, verbose_name='descripción formulario')
    formulario_boton_principal_contacto = models.CharField(max_length=255, verbose_name='botón formulario')
    etiqueta_nombre_contacto = models.CharField(max_length=255, verbose_name='etiqueta nombre')
    etiqueta_email_contacto = models.CharField(max_length=255, verbose_name='etiqueta email')
    etiqueta_telefono_contacto = models.CharField(max_length=255, verbose_name='etiqueta phone')
    etiqueta_tipo_de_negocio_contacto = models.CharField(max_length=255, verbose_name='etiqueta tipo de negocio')
    etiqueta_mensaje_contacto = models.CharField(max_length=255, verbose_name='etiqueta mensaje')
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
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='nombre')
    etiqueta_email = models.CharField(max_length=255, verbose_name='email')
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='mensaje')
    cuarta_seccion_imagen = models.ImageField(upload_to='CentrodeAyuda', verbose_name='imagen')
    
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
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    primera_seccion_subtitulo = models.CharField(max_length=255, verbose_name='subtítulo', default='')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', default='')
    
    segunda_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    segunda_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', default='')
    
    tercera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    tercera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', default='')
    
    class Meta:
        verbose_name = 'Condición de Servicio'
        verbose_name_plural = 'Condiciones de Servicio'

class TerminosdeServicioPunto(models.Model):
    terminos_de_servicio = models.ForeignKey(TerminosdeServicio, on_delete=models.CASCADE, verbose_name='Términos de Servicio')
    titulo = models.CharField(max_length=255, verbose_name='título de término', default='')
    descripcion = models.TextField(blank=True, verbose_name='descripción de término', default='')
    class Meta:
        verbose_name = 'Punto de Condición de Servicio'
        verbose_name_plural = 'Puntos de Condiciones de Servicio'
        
#Contactanos
class Contactanos(BaseModel):
    formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario')
    formulario_descripcion = models.TextField(blank=True, verbose_name='descripción de formulario')
    formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario')
    etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre')
    etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email')
    etiqueta_mensaje = models.CharField(max_length=255, verbose_name='etiqueta mensaje')
    primera_seccion_titulo = models.CharField(max_length=255, verbose_name='título', default='')
    primera_seccion_descripcion = models.TextField(blank=True, verbose_name='descripción', default='')
    
    tercera_seccion_imagen = models.ImageField(upload_to='contactanos', verbose_name='imagen')
    tercera_seccion_formulario_titulo = models.CharField(max_length=255, verbose_name='título de formulario')
    tercera_seccion_formulario_boton_principal = models.CharField(max_length=255, verbose_name='botón de formulario')
    tercera_seccion_etiqueta_nombre = models.CharField(max_length=255, verbose_name='etiqueta nombre')
    tercera_seccion_etiqueta_email = models.CharField(max_length=255, verbose_name='etiqueta email')
    tercera_seccion_etiqueta_comentario = models.CharField(max_length=255, verbose_name='etiqueta comentario')
    
    class Meta:
        verbose_name = 'Contáctanos'
        verbose_name_plural = 'Contáctanos'
        
class Datos(models.Model):
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto')
    imagen = models.ImageField(upload_to='datos', verbose_name='imagen')
    titulo = models.CharField(max_length=255, verbose_name='título', default='')
    primera_descripcion = models.TextField(blank=True, verbose_name='primera descripción', default='')
    segunda_descripcion = models.TextField(blank=True, verbose_name='segunda descripción', default='')
    

    class Meta:
        verbose_name = 'Contáctanos Datos'
        verbose_name_plural = 'Contáctanos Datos'

class Iconos(models.Model):
    contactanos = models.ForeignKey(Contactanos, on_delete=models.CASCADE, verbose_name='Contacto')
    icono = models.ImageField(upload_to='iconos', verbose_name='imagen')

    class Meta:
        verbose_name = 'Íconos'
        verbose_name_plural = 'Íconos'