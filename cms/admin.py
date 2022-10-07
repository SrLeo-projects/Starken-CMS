from django.contrib import admin

from cms.models import *


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion','titulo_imagen', 'alt_imagen', 'imagen', 'boton', 'boton_url')
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
                ('primera_seccion_titulo_imagen', 'primera_seccion_alt_imagen'),
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
                ('cuarta_seccion_tarjeta_1_titulo_imagen', 'cuarta_seccion_tarjeta_1_alt_imagen'),
                'cuarta_seccion_tarjeta_1_imagen',
                ('cuarta_seccion_tarjeta_2_titulo_imagen', 'cuarta_seccion_tarjeta_2_alt_imagen'),
                'cuarta_seccion_tarjeta_2_imagen',
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
                ('quinta_seccion_titulo_imagen', 'quinta_seccion_alt_imagen'),
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
                ('primera_seccion_titulo_imagen', 'primera_seccion_alt_imagen'),
                'primera_seccion_imagen',
                'primera_seccion_contenido',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('segunda_seccion_titulo_imagen', 'segunda_seccion_alt_imagen'),
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
                ('primera_seccion_titulo_imagen', 'primera_seccion_alt_imagen'),
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
    filter_horizontal = ['tercera_seccion_preguntas']
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
                ('cuarta_seccion_titulo_imagen', 'cuarta_seccion_alt_imagen'),
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
    filter_horizontal = ['segunda_seccion_preguntas']
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
                'segunda_seccion_preguntas',
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
                ('tercera_seccion_titulo_imagen', 'tercera_seccion_alt_imagen'),
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
    
    
class BotonInline(admin.StackedInline):
    model = Boton
    extra = 0
   
class AdvertenciaInline(admin.StackedInline):
    model = Advertencia
    extra = 0 

@admin.register(Cotizador)
class CotizadorAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_titulo',
                'primera_seccion_destacado',
                'etiqueta_origen',
                'etiqueta_destino',
                'etiqueta_encomienda',
                'etiqueta_dimensiones',
                'etiqueta_peso',
                'etiqueta_servicio',
                'etiqueta_tipo_de_entrega',
                'boton_principal'
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_titulo',
                'segunda_seccion_advertencia',
            )
        }),
    )
    
    inlines = [BotonInline, AdvertenciaInline]
    
    

class AccionInline(admin.StackedInline):
    model = Accion
    extra = 0
   
class ModalidadesInline(admin.StackedInline):
    model = Modalidades
    extra = 0 

@admin.register(DHL)
class DHLAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_subtitulo',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_imagen',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_contenido',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_titulo',
                'cuarta_seccion_destacado',
                'cuarta_seccion_descripcion',
                'cuarta_seccion_boton',
                'cuarta_seccion_boton_url',
            )
        }),
    )
    
    inlines = [ModalidadesInline, AccionInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Modalidades de Servicio", "Tercera Sección", "Cuarta Sección", "Acciones")
    


class EmpresasBeneficiosInline(admin.StackedInline):
    model = EmpresasBeneficios
    extra = 0
   
class EmpresasCarruselInline(admin.StackedInline):
    model = EmpresasCarrusel
    extra = 0 

@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_imagen',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_imagen_fondo',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email',  
                'etiqueta_telefono', 
                'etiqueta_tipo_de_negocio',
                'tercera_seccion_imagen',
                'tercera_seccion_titulo',
                'tercera_seccion_descripcion',
                'tercera_seccion_boton',
                'tercera_seccion_boton_url',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_imagen',
                'cuarta_seccion_titulo',
                'cuarta_seccion_descripcion',
                'cuarta_seccion_titulo_interno',
                'cuarta_seccion_subtitulo_interno',
                'cuarta_seccion_primer_boton',
                'cuarta_seccion_primer_boton_url',
                'cuarta_seccion_segundo_boton',
                'cuarta_seccion_segundo_boton_url',
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_imagen',
                'quinta_seccion_titulo',
                'quinta_seccion_descripcion',
                'quinta_seccion_boton',
                'quinta_seccion_boton_url',
            )
        }),
    )
    
    inlines = [EmpresasCarruselInline, EmpresasBeneficiosInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Beneficios", "Tercera Sección", "Imágenes", "Cuarta Sección", "Quinta Sección")
    
    

class EnviosInternacionalesBeneficiosInline(admin.StackedInline):
    model = EnviosInternacionalesBeneficios
    extra = 0

@admin.register(EnviosInternacionales)
class EnviosInternacionalesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_subtitulo',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_imagen',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_imagen_primer_bloque',
                'tercera_seccion_titulo_primer_bloque',
                'tercera_seccion_descripcion_primer_bloque',
                'tercera_seccion_boton_primer_bloque',
                'tercera_seccion_boton_url_primer_bloque',
                'tercera_seccion_imagen_segundo_bloque',
                'tercera_seccion_titulo_segundo_bloque',
                'tercera_seccion_descripcion_segundo_bloque',
                'tercera_seccion_boton_segundo_bloque',
                'tercera_seccion_boton_url_segundo_bloque',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_imagen',
                'cuarta_seccion_titulo',
                'cuarta_seccion_destacado',
                'cuarta_seccion_descripcion',
                'cuarta_seccion_boton',
                'cuarta_seccion_boton_url',
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_imagen',
                'quinta_seccion_titulo',
                'quinta_seccion_descripcion',
                'quinta_seccion_boton',
                'quinta_seccion_boton_url',
            )
        }),
    )
    
    inlines = [EnviosInternacionalesBeneficiosInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Beneficios", "Tercera Sección", "Cuarta Sección", "Quinta Sección")
    
    
    
    
class EnviosNacionalesBeneficiosInline(admin.StackedInline):
    model = EnviosNacionalesBeneficios
    extra = 0

class EnviosNacionalesRecomendacionesInline(admin.StackedInline):
    model = EnviosNacionalesRecomendaciones
    extra = 0

@admin.register(EnviosNacionales)
class EnviosNacionalesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_subtitulo',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_imagen',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_imagen',
                'tercera_seccion_titulo',
                'tercera_seccion_destacado',
                'tercera_seccion_descripcion',
                'tercera_seccion_boton',
                'tercera_seccion_boton_url',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_imagen',
                'cuarta_seccion_titulo',
                'cuarta_seccion_destacado',
                'cuarta_seccion_subtitulo',
                'cuarta_seccion_boton',
                'cuarta_seccion_boton_url',
            )
        }),
    )
    
    inlines = [EnviosNacionalesBeneficiosInline, EnviosNacionalesRecomendacionesInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Beneficios", "Tercera Sección", "Cuarta Sección", "Recomendaciones")
    
    

class MiPrimerEnvioStepInline(admin.StackedInline):
    model = MiPrimerEnvioStep
    extra = 0

@admin.register(MiPrimerEnvio)
class MiPrimerEnvioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_imagen',
            )
        }),
       
    )
    
    inlines = [MiPrimerEnvioStepInline]
    jazzmin_section_order = ("General", "Primera Sección", "Indicaciones")
    
    
    
class MypymesBeneficiosInline(admin.StackedInline):
    model = MypymesBeneficios
    extra = 0
   
class MypymesIndicacionesInline(admin.StackedInline):
    model = MypymesIndicaciones
    extra = 0 

class MypymesTestimoniosInline(admin.StackedInline):
    model = MypymesTestimonios
    extra = 0 

@admin.register(Mypymes)
class MypymesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_imagen',
                'primera_seccion_video',
                'primera_seccion_miniatura',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_imagen_fondo',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email',  
                'etiqueta_telefono', 
                'etiqueta_tipo_de_negocio',
                'tercera_seccion_imagen',
                'tercera_seccion_titulo',
                'tercera_seccion_descripcion',
                'tercera_seccion_enlace',
                'tercera_seccion_enlace_url',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_titulo',
                'cuarta_seccion_destacado',
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_titulo',
                'quinta_seccion_destacado',
            )
        }),
        ('Sexta Sección', {
            'fields': (
                'sexta_seccion_imagen',
                'sexta_seccion_titulo',
                'sexta_seccion_descripcion',
                'sexta_seccion_titulo_interno',
                'sexta_seccion_subtitulo_interno',
                'sexta_seccion_primer_boton',
                'sexta_seccion_primer_boton_url',
                'sexta_seccion_segundo_boton',
                'sexta_seccion_segundo_boton_url',
            )
        }),
        ('Séptima Sección', {
            'fields': (
                'septima_seccion_imagen',
                'septima_seccion_titulo',
                'septima_seccion_descripcion',
                'septima_seccion_boton',
                'septima_seccion_boton_url',
            )
        }),
    )
    
    inlines = [MypymesIndicacionesInline, MypymesBeneficiosInline, MypymesTestimoniosInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Beneficios", "Tercera Sección", "Cuarta Sección", "Indicaciones", "Quinta Sección", "Testimonios", "Sexta Sección", "Séptima Sección")