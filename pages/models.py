from django.db import models

class URL(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='nombre de la URL', null=True, blank=True)
    url = models.CharField(max_length=255, verbose_name='URL', null=True, blank=True)
    
    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URL'
    
    def __str__(self):
            return f'{self.nombre} - {self.url}'

class BasicSeccion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    destacado = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    subtitulo = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    primer_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_boton_basic', null=True, blank=True)
    segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segundo_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_boton_basic', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='basic_seccion', verbose_name='imagen', null=True, blank=True)
    invertir_sentido= models.BooleanField(default=False, verbose_name='invertir sentido')

    def __str__(self):
        return self.titulo

class VideoSeccion(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.titulo

class BenefitSeccion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
    
class Benefit(models.Model):
    seccion = models.ForeignKey(BenefitSeccion, on_delete=models.CASCADE, related_name='benefits')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='benefit_seccion', verbose_name='imagen', null=True, blank=True)

    def __str__(self):
        return self.titulo

class BannerSeccion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    destacado = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    subtitulo = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    primer_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_boton_banner', null=True, blank=True)
    segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segundo_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_boton_banner', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='banner_seccion', verbose_name='imagen', null=True, blank=True)
    titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    imagen_movil = models.ImageField(upload_to='banner_seccion', verbose_name='imagen móvil', null=True, blank=True)
    
    def __str__(self):
        return self.titulo

class BloquesSeccion(models.Model):
    primer_bloque_titulo = models.CharField(max_length=200, verbose_name='titulo primer bloque', null=True, blank=True)
    primer_bloque_descripcion = models.TextField(null=True, verbose_name='descripción primer bloque', blank=True)
    primer_bloque_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    primer_bloque_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del primer botón', related_name='url_primer_bloque_boton', null=True, blank=True)
    primer_bloque_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen primer bloque', null=True, blank=True)
    primer_bloque_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen primer bloque', null=True, blank=True)
    primer_bloque_imagen = models.ImageField(upload_to='bloques_seccion', verbose_name='imagen primer bloque', null=True, blank=True)
    
    segundo_bloque_titulo = models.CharField(max_length=200, verbose_name='titulo segundo bloque', null=True, blank=True)
    segundo_bloque_descripcion = models.TextField(null=True, verbose_name='descripción segundo bloque', blank=True)
    segundo_bloque_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segundo_bloque_boton_url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url del segundo botón', related_name='url_segundo_bloque_boton', null=True, blank=True)
    segundo_bloque_titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen segundo bloque', null=True, blank=True)
    segundo_bloque_alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen segundo bloque', null=True, blank=True)
    segundo_bloque_imagen = models.ImageField(upload_to='bloques_seccion', verbose_name='imagen segundo bloque', null=True, blank=True)
    
    
class Etiqueta(models.Model):
    etiqueta = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.etiqueta

class FormularioSeccion(models.Model):
    primer_titulo = models.CharField(max_length=200, verbose_name='primer título', null=True, blank=True)
    primera_descripcion = models.TextField(null=True, verbose_name='primera descripción', blank=True)
    etiqueta = models.ManyToManyField(Etiqueta, verbose_name='etiquetas', blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    titulo_imagen_fondo = models.CharField(max_length=255, verbose_name='título imagen de fondo', null=True, blank=True)
    alt_imagen_fondo = models.CharField(max_length=255, verbose_name='alt imagen de fondo', null=True, blank=True)
    imagen_fondo = models.ImageField(upload_to='formulario_seccion', verbose_name='imagen de fondo', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='formulario_seccion', verbose_name='imagen', null=True, blank=True)
    segundo_titulo = models.CharField(max_length=200, verbose_name='segundo título', null=True, blank=True)
    segunda_descripcion = models.TextField(null=True, verbose_name='segunda descripción', blank=True)
    destacado = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    url = models.ForeignKey(URL, on_delete=models.CASCADE, verbose_name='url', related_name='url_formulario', null=True, blank=True)

    def __str__(self):
        return self.primer_titulo
    
class Page(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    header = models.BooleanField(default=False)
    footer= models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class PageDetail(models.Model):
    class Type(models.IntegerChoices):
        BASIC_SECCION = 1
        VIDEO_SECCION = 2
        BENEFIT_SECCION = 3
        BANNER_SECCION = 4
        FORMULARIO_SECCION = 5
        BLOQUES_SECCION = 6

    pagina = models.ForeignKey(Page, on_delete=models.CASCADE)
    type = models.IntegerField(choices=Type.choices)
    basic_seccion = models.ForeignKey(BasicSeccion, on_delete=models.CASCADE, null=True, blank=True)
    video_seccion = models.ForeignKey(VideoSeccion, on_delete=models.CASCADE, null=True, blank=True)
    benefit_seccion = models.ForeignKey(BenefitSeccion, on_delete=models.CASCADE, null=True, blank=True)
    banner_seccion = models.ForeignKey(BannerSeccion, on_delete=models.CASCADE, null=True, blank=True)
    formulario_seccion = models.ForeignKey(FormularioSeccion, on_delete=models.CASCADE, null=True, blank=True)
    bloques_seccion = models.ForeignKey(BloquesSeccion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.page.titulo