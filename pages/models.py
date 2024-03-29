from django.db import models
from cms.models import URL
from faicon.fields import FAIconField
from django.utils.text import slugify
class BannerSeccion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    destacado = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    subtitulo = models.CharField(max_length=200, verbose_name='subtítulo', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    primer_boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del primer botón', related_name='url_primer_boton_banner', null=True, blank=True)
    primer_boton_icono = FAIconField(verbose_name='ícono primer botón', null=True, blank=True)
    segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segundo_boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del segundo botón', related_name='url_segundo_boton_banner', null=True, blank=True)
    segundo_boton_icono = FAIconField(verbose_name='ícono segundo botón', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='banner_seccion', verbose_name='imagen', null=True, blank=True)
    titulo_imagen_movil = models.CharField(max_length=255, verbose_name='título imagen móvil', null=True, blank=True)
    alt_imagen_movil = models.CharField(max_length=255, verbose_name='alt imagen móvil', null=True, blank=True)
    imagen_movil = models.ImageField(upload_to='banner_seccion', verbose_name='imagen móvil', null=True, blank=True)
    
    def __str__(self):
        return str(self.titulo)
    
class Beneficio(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='beneficio_seccion', verbose_name='imagen', null=True, blank=True)
    boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del botón', related_name='url_boton_beneficio', null=True, blank=True)
    boton_icono = FAIconField(verbose_name='ícono botón', null=True, blank=True)

    def __str__(self):
        return str(self.titulo)
    
class BeneficioSeccion(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    beneficios = models.ManyToManyField(Beneficio, verbose_name='Beneficios', blank=True)

    def __str__(self):
        return str(self.titulo)

class BasicoSeccion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    destacado = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    subtitulo = models.CharField(max_length=200, verbose_name='subtítulo', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    primer_boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del primer botón', related_name='url_primer_boton_basico', null=True, blank=True)
    primer_boton_icono = FAIconField(verbose_name='ícono primer botón', null=True, blank=True)
    segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segundo_boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del segundo botón', related_name='url_segundo_boton_basico', null=True, blank=True)
    segundo_boton_icono = FAIconField(verbose_name='ícono segundo botón', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='basico_seccion', verbose_name='imagen', null=True, blank=True)
    invertir_sentido= models.IntegerField(choices=[
        (0, 'IMAGEN A LA IZQUIERDA'),
        (1, 'IMAGEN A LA DERECHA'),
    ], default=1, null=True, blank=True, verbose_name='Posición de la Imagen')

    def __str__(self):
        return str(self.titulo)
    
class Servicio(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del primer botón', related_name='url_boton_servicios_pages', null=True, blank=True)
    boton_icono = FAIconField(verbose_name='ícono botón', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='servicio_seccion', verbose_name='imagen', null=True, blank=True)
    
    def __str__(self):
        return str(self.titulo)

class ServiciosSeccion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    destacado = models.CharField(max_length=200, verbose_name='destacado', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    primer_boton = models.CharField(max_length=255, verbose_name='primer botón', null=True, blank=True)
    primer_boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del primer botón', related_name='url_primer_boton_servicios_pages', null=True, blank=True)
    primer_boton_icono = FAIconField(verbose_name='ícono primer botón', null=True, blank=True)
    segundo_boton = models.CharField(max_length=255, verbose_name='segundo botón', null=True, blank=True)
    segundo_boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del segundo botón', related_name='url_segundo_boton_servicios_pages', null=True, blank=True)
    segundo_boton_icono = FAIconField(verbose_name='ícono segundo botón', null=True, blank=True)
    servicios = models.ManyToManyField(Servicio, verbose_name='Servicios', blank=True)
    
    def __str__(self):
        return str(self.titulo)

    

class Bloques(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    boton = models.CharField(max_length=255, verbose_name='botón', null=True, blank=True)
    boton_url = models.ForeignKey(URL, on_delete=models.SET_NULL, verbose_name='url del botón', related_name='url_boton_bloque', null=True, blank=True)
    boton_icono = FAIconField(verbose_name='ícono botón', null=True, blank=True)
    titulo_imagen = models.CharField(max_length=255, verbose_name='título imagen', null=True, blank=True)
    alt_imagen = models.CharField(max_length=255, verbose_name='alt imagen', null=True, blank=True)
    imagen = models.ImageField(upload_to='bloques_seccion', verbose_name='imagen', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    def __str__(self):
        return str(self.titulo)
    
    
class BloquesSeccion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    bloques = models.ManyToManyField(Bloques, verbose_name='Bloques', blank=True)
    
    def __str__(self):
        return str(self.titulo)
    

class Formulario(models.Model):
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    nombre = models.CharField(max_length=200, verbose_name='nombre', null=True, blank=True)
    
    def __str__(self):
        return str(self.nombre)
       
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Formulario, self).save(*args, **kwargs)

class OpcionGrupo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='nombre', null=True, blank=True)
    
    def __str__(self):
        return str(self.nombre)

class Opcion(models.Model):
    grupo = models.ForeignKey(OpcionGrupo, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=200, verbose_name='nombre', null=True, blank=True)
    
    def __str__(self):
        return f'{self.grupo} - {self.nombre}'
        
class Campo(models.Model):
    class TypeCampo(models.IntegerChoices):
        TEXT = 1
        TEXTAREA = 2
        NUMBER = 3
        BOOLEAN = 4
        DATE = 5
        TIME = 6
        FILE = 7
    
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=TypeCampo.choices, null=True, blank=True)
    label = models.CharField(max_length=200, verbose_name='label', null=True, blank=True)
    opciones = models.ManyToManyField(Opcion, blank=True)
    
    def __str__(self):
        return str(self.label)
    
class Resultado(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(verbose_name='fecha de creación', null=True, blank=True)
    
    def __str__(self):
        return str(self.created_at)
    
    def datos(self):
        return ', '.join([f'{detail.campo.label}: {detail.valor}' for detail in self.details.all()])

class ResultadoDetalle(models.Model):
    resultado = models.ForeignKey(Resultado,related_name='details', on_delete=models.CASCADE, null=True, blank=True)
    campo = models.ForeignKey(Campo,verbose_name='campo', on_delete=models.CASCADE, null=True, blank=True)
    valor = models.CharField(max_length=200, verbose_name='valor', null=True, blank=True)
    
    def __str__(self):
        return str(self.valor)
    
class FormularioSeccion(models.Model):
    formulario = models.ForeignKey(Formulario,related_name='formulario', on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200, verbose_name='título', null=True, blank=True)
    descripcion = models.TextField(null=True, verbose_name='descripción', blank=True)
    
    def __str__(self):
        return str(self.titulo)
    
class Page(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True) 
    header = models.BooleanField(default=False)
    footer= models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.titulo)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Page, self).save(*args, **kwargs)
        

class EtiquetasMeta(models.Model):

    pagina = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='name', null=True, blank=True)
    content = models.CharField(max_length=200, verbose_name='content',null=True, blank=True)
    property = models.CharField(max_length=200, verbose_name='property', null=True, blank=True)
    itemprop = models.CharField(max_length=200, verbose_name='itemprop', null=True, blank=True)

    def __str__(self):
        return str(self.pagina.titulo)
        
        
class PageDetail(models.Model):
    class Type(models.IntegerChoices):
        BANNER_SECCION = 1
        BENEFICIO_SECCION = 2
        BASICO_SECCION = 3
        SERVICIOS_SECCION = 4
        BLOQUES_SECCION = 5
        FORMULARIO_SECCION = 6

    pagina = models.ForeignKey(Page, on_delete=models.CASCADE)
    type = models.IntegerField(choices=Type.choices)
    banner_seccion = models.ForeignKey(BannerSeccion, on_delete=models.SET_NULL, null=True, blank=True)
    beneficio_seccion = models.ForeignKey(BeneficioSeccion, on_delete=models.SET_NULL, null=True, blank=True)
    basico_seccion = models.ForeignKey(BasicoSeccion, on_delete=models.SET_NULL, null=True, blank=True)
    servicios_seccion = models.ForeignKey(ServiciosSeccion, on_delete=models.SET_NULL, null=True, blank=True)
    bloques_seccion = models.ForeignKey(BloquesSeccion, on_delete=models.SET_NULL, null=True, blank=True)
    formulario_seccion = models.ForeignKey(FormularioSeccion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.pagina.titulo)
