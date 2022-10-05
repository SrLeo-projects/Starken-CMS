from django.contrib import admin

from cms.models import *


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'imagen', 'boton', 'boton_url')
    list_filter = ('titulo', 'descripcion', 'imagen', 'boton', 'boton_url')

class BannerInline(admin.StackedInline):
    model = Banner
    extra = 0

class OpcionInline(admin.StackedInline):
    model = Opcion
    extra = 0

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']
    
    filter_horizontal = ['servicios']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                ('primera_seccion_titulo', 'primera_seccion_destacado'),
                'primera_seccion_descripcion',
                ('primera_seccion_boton_principal', 'primera_seccion_boton_principal_url'),
                ('primera_seccion_boton_secundario', 'primera_seccion_boton_secundario_url'),
                'primera_seccion_imagen',
                ('primera_seccion_subtitulo', 'primera_seccion_subtitulo_descripcion'),
                ('primera_seccion_link', 'primera_seccion_link_texto'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
                ('segunda_seccion_boton_principal', 'segunda_seccion_boton_principal_url'),
                'servicios',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
                'tercera_seccion_descripcion',
                ('tercera_seccion_boton_principal', 'tercera_seccion_boton_principal_url'),
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                ('cuarta_seccion_tarjeta_1_imagen', 'cuarta_seccion_tarjeta_2_imagen'),
                ('cuarta_seccion_tarjeta_1_titulo', 'cuarta_seccion_tarjeta_2_titulo'),
                ('cuarta_seccion_tarjeta_1_descripcion', 'cuarta_seccion_tarjeta_2_descripcion'),
                ('cuarta_seccion_tarjeta_1_boton', 'cuarta_seccion_tarjeta_2_boton'),
                ('cuarta_seccion_tarjeta_1_boton_url', 'cuarta_seccion_tarjeta_2_boton_url'),
            )
        }),
        ('Quinta Sección', {
            'fields': (
                ('quinta_seccion_titulo', 'quinta_seccion_palabras'),
                'quinta_seccion_descripcion',
                ('quinta_seccion_boton_principal', 'quinta_seccion_boton_principal_url'),
            )
        }),
    )

    inlines = [BannerInline, OpcionInline]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                ('primera_seccion_imagen', 'primera_seccion_titulo'),
                'primera_seccion_descripcion',
                ('primera_seccion_boton_principal', 'primera_seccion_boton_principal_url'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
                'tercera_seccion_descripcion',
                ('tercera_seccion_boton_principal', 'tercera_seccion_boton_principal_url'),
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                ('cuarta_seccion_titulo', 'cuarta_seccion_destacado'),
                'cuarta_seccion_descripcion',
                ('cuarta_seccion_boton_principal', 'cuarta_seccion_boton_principal_url'),
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_imagen',
                ('quinta_seccion_titulo', 'quinta_seccion_destacado'),
                'quinta_seccion_subtitulo',
                'quinta_seccion_descripcion',
                ('quinta_seccion_boton_principal', 'quinta_seccion_boton_principal_url'),
            )
        }),
    )


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'primera_seccion_fecha_de_creacion']
    search_fields = ['titulo']
    list_filter = ['tipo']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'tipo',
                'primera_seccion_etiqueta',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_fecha_de_creacion',
                'primera_seccion_imagen',
                'primera_seccion_contenido',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_imagen',
                'segunda_seccion_titulo',
                'segunda_seccion_primer_boton',
                'segunda_seccion_url_primer_boton',
                'segunda_seccion_segundo_boton',
                'segunda_seccion_url_segundo_boton',
            )
        }),
    )
    
    
class StarkenProBeneficioInline(admin.StackedInline):
    model = StarkenProBeneficio
    extra = 0

class StarkenProPasoInline(admin.StackedInline):
    model = StarkenProPaso
    extra = 0

@admin.register(StarkenPro)
class StarkenProAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_imagen',
                ('primera_seccion_titulo', 'primera_seccion_destacado'),
                'primera_seccion_descripcion',
                ('primera_seccion_boton_principal', 'primera_seccion_boton_principal_url'),
                'primera_seccion_mensaje',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email', 
                'etiqueta_mensaje'
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
            )
        }),
    )

    inlines = [StarkenProBeneficioInline, StarkenProPasoInline]
    

class CentrodeAyudaBeneficioInline(admin.StackedInline):
    model = CentrodeAyudaBeneficio
    extra = 0    

@admin.register(CentrodeAyuda)
class CentrodeAyudaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                ('primera_seccion_boton_principal', 'primera_seccion_boton_principal_url'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
                'formulario_titulo_contacto',
                'formulario_descripcion_contacto',
                'formulario_boton_principal_contacto',
                'etiqueta_nombre_contacto', 
                'etiqueta_email_contacto', 
                'etiqueta_mensaje_contacto', 
                'etiqueta_telefono_contacto', 
                'etiqueta_tipo_de_negocio_contacto'
            )
        }),
        ('Tercera Sección', {
            'fields': (
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
                'tercera_seccion_descripcion',
                ('tercera_seccion_boton_principal', 'tercera_seccion_boton_principal_url'),
                'tercera_seccion_preguntas',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_imagen',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email', 
                'etiqueta_mensaje',
            )
        }),
    )

    inlines = [CentrodeAyudaBeneficioInline]
    

class TerminosdeServicioPuntoInline(admin.StackedInline):
    model = TerminosdeServicioPunto
    extra = 0
    
class TerminosdeServicioSeccionInline(admin.StackedInline):
    model = TerminosdeServicioSeccion
    extra = 0

@admin.register(TerminosdeServicio)
class TerminosdeServicioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_titulo',
                'primera_seccion_subtitulo',
                'primera_seccion_descripcion',
            )
        }),
    )

    inlines = [TerminosdeServicioPuntoInline, TerminosdeServicioSeccionInline]    

class PreguntasInline(admin.StackedInline):
    model = Preguntas
    extra = 0
    
@admin.register(PreguntasCategoria)
class PreguntasCategoriaInline(admin.ModelAdmin):
    model = PreguntasCategoria
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion', 'titulo_categoria')
        }),
    )
    
    inlines = [PreguntasInline]

@admin.register(PreguntasFrecuentes)
class PreguntasFrecuentesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_titulo',
                'primera_seccion_boton_buscar',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_categoria',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_titulo',
                'tercera_seccion_descripcion',
                'tercera_seccion_titulo_primer_bloque',
                'tercera_seccion_descripcion_primer_bloque',
                'tercera_seccion_titulo_segundo_bloque',
                'tercera_seccion_descripcion_segundo_bloque',
            )
        }),
    )
    

class DatosInline(admin.StackedInline):
    model = Datos
    extra = 0
   
class IconosInline(admin.StackedInline):
    model = Iconos
    extra = 0 

@admin.register(Contactanos)
class ContactanosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email', 
                'etiqueta_mensaje',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_imagen',
                'tercera_seccion_formulario_titulo',
                'tercera_seccion_formulario_boton_principal',
                'tercera_seccion_etiqueta_nombre', 
                'tercera_seccion_etiqueta_email', 
                'tercera_seccion_etiqueta_comentario',
            )
        }),
    )
    
    inlines = [DatosInline, IconosInline]
    jazzmin_section_order = ("General", "Primera Sección", "Íconos", "Contáctanos Datos", "Tercera Sección")