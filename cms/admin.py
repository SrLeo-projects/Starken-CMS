from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from tabular_export.admin import export_to_csv_action, export_to_excel_action
from cms.models import *
from django import forms
from django_select2 import forms as s2forms


@admin.register(Notificacion)
class NotificacionAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('tipo', 'descripcion','fecha_de_caducidad')
    list_filter = ('tipo',)


@admin.register(Servicio)
class ServicioAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'descripcion','titulo_imagen', 'alt_imagen', 'imagen', 'boton', 'boton_url')
    list_filter = ('titulo', 'descripcion', 'imagen', 'boton', 'boton_url')

class BannerInline(admin.StackedInline):
    model = Banner
    extra = 0

class OpcionInline(admin.StackedInline):
    model = Opcion
    extra = 0

@admin.register(URL)
class URLAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['nombre']


@admin.register(Home)
class HomeAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion', 'primera_seccion_boton_principal_url']
    filter_horizontal = ['servicios']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
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
                'segunda_seccion_ocultar',
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
                ('segunda_seccion_boton_principal', 'segunda_seccion_boton_principal_url'),
                'servicios',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
                'tercera_seccion_descripcion',
                ('tercera_seccion_boton_principal', 'tercera_seccion_boton_principal_url'),
                ('tercera_seccion_titulo_imagen', 'tercera_seccion_alt_imagen'),
                'tercera_seccion_imagen',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                ('cuarta_seccion_tarjeta_1_titulo_imagen', 'cuarta_seccion_tarjeta_1_alt_imagen'),
                'cuarta_seccion_tarjeta_1_imagen',
                'cuarta_seccion_tarjeta_1_titulo',
                'cuarta_seccion_tarjeta_1_descripcion',
                'cuarta_seccion_tarjeta_1_boton',
                'cuarta_seccion_tarjeta_1_boton_url',
                ('cuarta_seccion_tarjeta_2_titulo_imagen', 'cuarta_seccion_tarjeta_2_alt_imagen'),
                'cuarta_seccion_tarjeta_2_imagen',
                'cuarta_seccion_tarjeta_2_titulo',
                'cuarta_seccion_tarjeta_2_descripcion',
                'cuarta_seccion_tarjeta_2_boton',
                'cuarta_seccion_tarjeta_2_boton_url',
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_ocultar',
                ('quinta_seccion_titulo', 'quinta_seccion_palabras'),
                'quinta_seccion_descripcion',
                ('quinta_seccion_boton_principal', 'quinta_seccion_boton_principal_url'),
                ('quinta_seccion_titulo_imagen', 'quinta_seccion_alt_imagen'),
                'quinta_seccion_imagen',
            )
        }),
    )
        
    inlines = [BannerInline, OpcionInline]

@admin.register(About)
class AboutAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo_imagen_movil',
                'primera_seccion_alt_imagen_movil',
                'primera_seccion_imagen_movil',
                'primera_seccion_titulo',
                'primera_seccion_subtitulo',
                'primera_seccion_descripcion',
                ('primera_seccion_boton_principal', 'primera_seccion_boton_principal_url'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
                'tercera_seccion_descripcion',
                ('tercera_seccion_boton_principal', 'tercera_seccion_boton_principal_url'),
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                ('cuarta_seccion_titulo', 'cuarta_seccion_destacado'),
                'cuarta_seccion_descripcion',
                ('cuarta_seccion_boton_principal', 'cuarta_seccion_boton_principal_url'),
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_ocultar',
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
class ArticuloAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'tipo', 'primera_seccion_fecha_de_creacion', 'slug']
    search_fields = ['titulo']
    list_filter = ['tipo']
    readonly_fields = ('slug',)
    fieldsets = (
        ('General', {
            'fields': ('tipo', 'titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
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
                'segunda_seccion_ocultar',
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
class StarkenProAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
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
                'segunda_seccion_ocultar',
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
                'tercera_seccion_descripcion',
            )
        }),
    )

    inlines = [StarkenProBeneficioInline, StarkenProPasoInline]
    

class CentrodeAyudaBeneficioInline(admin.StackedInline):
    model = CentrodeAyudaBeneficio
    extra = 0    

@admin.register(CentrodeAyuda)
class CentrodeAyudaAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    filter_horizontal = ['segunda_seccion_preguntas']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                ('primera_seccion_boton_principal', 'primera_seccion_boton_principal_url'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
                ('segunda_seccion_boton_principal', 'segunda_seccion_boton_principal_url'),
                'segunda_seccion_preguntas',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                ('tercera_seccion_titulo_imagen', 'tercera_seccion_alt_imagen'),
                'tercera_seccion_imagen',
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
class TerminosdeServicioAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
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
class PreguntasCategoriaInline(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    model = PreguntasCategoria
    fieldsets = (
        ('General', {
            'fields': ('titulo_categoria', 'primera_seccion_ocultar',)
        }),
    )
    
    inlines = [PreguntasInline]

@admin.register(PreguntasFrecuentes)
class PreguntasFrecuentesAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    filter_horizontal = ['segunda_seccion_preguntas']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo',
                'primera_seccion_boton_buscar',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_preguntas',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
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
class ContactanosAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo_imagen_movil',
                'primera_seccion_alt_imagen_movil',
                'primera_seccion_imagen_movil',
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
                'tercera_seccion_ocultar',
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
class CotizadorAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
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
                'segunda_seccion_ocultar',
                'segunda_seccion_titulo',
                'segunda_seccion_boton_principal',
                'segunda_seccion_boton_principal_destacado',
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
class DHLAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_subtitulo',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo_imagen_movil',
                'primera_seccion_alt_imagen_movil',
                'primera_seccion_imagen_movil',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_contenido',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
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
class EmpresasAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo_imagen_movil',
                'primera_seccion_alt_imagen_movil',
                'primera_seccion_imagen_movil',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_titulo_imagen_fondo',
                'tercera_seccion_alt_imagen_fondo',
                'tercera_seccion_imagen_fondo',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email',  
                'etiqueta_telefono', 
                'etiqueta_tipo_de_negocio',
                'tercera_seccion_titulo_imagen',
                'tercera_seccion_alt_imagen',
                'tercera_seccion_imagen',
                'tercera_seccion_titulo',
                'tercera_seccion_descripcion',
                'tercera_seccion_enlace',
                'tercera_seccion_enlace_url',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                'cuarta_seccion_titulo_imagen',
                'cuarta_seccion_alt_imagen',
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
                'quinta_seccion_ocultar',
                'quinta_seccion_titulo_imagen',
                'quinta_seccion_alt_imagen',
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
class EnviosInternacionalesAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_subtitulo',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo_imagen_movil',
                'primera_seccion_alt_imagen_movil',
                'primera_seccion_imagen_movil',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_titulo_imagen_primer_bloque',
                'tercera_seccion_alt_imagen_primer_bloque',
                'tercera_seccion_imagen_primer_bloque',
                'tercera_seccion_titulo_primer_bloque',
                'tercera_seccion_descripcion_primer_bloque',
                'tercera_seccion_boton_primer_bloque',
                'tercera_seccion_boton_url_primer_bloque',
                'tercera_seccion_titulo_imagen_segundo_bloque',
                'tercera_seccion_alt_imagen_segundo_bloque',
                'tercera_seccion_imagen_segundo_bloque',
                'tercera_seccion_titulo_segundo_bloque',
                'tercera_seccion_descripcion_segundo_bloque',
                'tercera_seccion_boton_segundo_bloque',
                'tercera_seccion_boton_url_segundo_bloque',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                'cuarta_seccion_titulo_imagen',
                'cuarta_seccion_alt_imagen',
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
                'quinta_seccion_ocultar',
                'quinta_seccion_titulo_imagen',
                'quinta_seccion_alt_imagen',
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
class EnviosNacionalesAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_subtitulo',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo_imagen_movil',
                'primera_seccion_alt_imagen_movil',
                'primera_seccion_imagen_movil',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_titulo_imagen',
                'tercera_seccion_alt_imagen',
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
                'cuarta_seccion_ocultar',
                'cuarta_seccion_titulo_imagen',
                'cuarta_seccion_alt_imagen',
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
class MiPrimerEnvioAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
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
class MypymesAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo_imagen_movil',
                'primera_seccion_alt_imagen_movil',
                'primera_seccion_imagen_movil',
                'primera_seccion_video',
                'primera_seccion_titulo_imagen_miniatura',
                'primera_seccion_alt_imagen_miniatura',
                'primera_seccion_miniatura',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_subtitulo',
                'segunda_seccion_boton',
                'segunda_seccion_boton_url',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_titulo_imagen_fondo',
                'tercera_seccion_alt_imagen_fondo',
                'tercera_seccion_imagen_fondo',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email',  
                'etiqueta_telefono', 
                'etiqueta_tipo_de_negocio',
                'tercera_seccion_titulo_imagen',
                'tercera_seccion_alt_imagen',
                'tercera_seccion_imagen',
                'tercera_seccion_titulo',
                'tercera_seccion_descripcion',
                'tercera_seccion_enlace',
                'tercera_seccion_enlace_url',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                'cuarta_seccion_titulo',
                'cuarta_seccion_destacado',
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_ocultar',
                'quinta_seccion_titulo',
                'quinta_seccion_destacado',
            )
        }),
        ('Sexta Sección', {
            'fields': (
                'sexta_seccion_ocultar',
                'sexta_seccion_titulo_imagen',
                'sexta_seccion_alt_imagen',
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
                'septima_seccion_ocultar',
                'septima_seccion_titulo_imagen',
                'septima_seccion_alt_imagen',
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
    
    

@admin.register(Reclamos)
class ReclamosAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    filter_horizontal = ['tercera_seccion_preguntas']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_rut', 
                'etiqueta_nombre',
                'etiqueta_email',  
                'etiqueta_telefono', 
                'etiqueta_reclamo',
                
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_titulo',
                'tercera_seccion_subtitulo',
                'tercera_seccion_destacado',
                'tercera_seccion_enlace_url',
                'tercera_seccion_preguntas',
            )
        }),
    )
    
    
class RecomendacionesInline(admin.StackedInline):
    model = Recomendaciones
    extra = 0
    
@admin.register(RecomendacionesCategoria)
class RecomendacionesCategoriaInline(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    model = RecomendacionesCategoria
    list_display = ['titulo', 'descripcion']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion', 'titulo_categoria', 'primera_seccion_ocultar',)
        }),
    )
    
    inlines = [RecomendacionesInline]

@admin.register(RecomendacionesEmbalaje)
class RecomendacionesEmbalajeAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
            )
        }),
    )
    
    
class SeguimientoIndicacionesInline(admin.StackedInline):
    model = SeguimientoIndicaciones
    extra = 0
    

@admin.register(Seguimiento)
class SeguimientoAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                ('primera_seccion_titulo_imagen', 'primera_seccion_alt_imagen'),
                'primera_seccion_imagen',
                'primera_seccion_titulo',
                'primera_seccion_subtitulo',
                'primera_seccion_boton_principal',
                'primera_seccion_etiqueta_codigo',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                ('tercera_seccion_tarjeta_1_titulo_imagen', 'tercera_seccion_tarjeta_1_alt_imagen'),
                'tercera_seccion_tarjeta_1_imagen',
                'tercera_seccion_tarjeta_1_titulo',
                'tercera_seccion_tarjeta_1_descripcion',
                'tercera_seccion_tarjeta_1_boton',
                'tercera_seccion_tarjeta_1_boton_url',
                ('tercera_seccion_tarjeta_2_titulo_imagen', 'tercera_seccion_tarjeta_2_alt_imagen'),
                'tercera_seccion_tarjeta_2_imagen',
                'tercera_seccion_tarjeta_2_titulo',
                'tercera_seccion_tarjeta_2_descripcion',
                'tercera_seccion_tarjeta_2_boton',
                'tercera_seccion_tarjeta_2_boton_url',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                ('cuarta_seccion_titulo_imagen', 'cuarta_seccion_alt_imagen'),
                'cuarta_seccion_imagen',
                ('cuarta_seccion_titulo', 'cuarta_seccion_palabras'),
                'cuarta_seccion_descripcion',
                ('cuarta_seccion_boton_principal', 'cuarta_seccion_boton_principal_url'),
                
            )
        }),
    )
    
    inlines = [SeguimientoIndicacionesInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Indicaciones", "Tercera Sección", "Cuarta Sección")
    
    
    
@admin.register(Sucursales)
class SucursalesAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']

    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo',
                'primera_seccion_destacado',
                'primera_seccion_descripcion',
            )
        }),
    )
    
    
class CovidComunicadoInline(admin.StackedInline):
    model = CovidComunicado
    extra = 0
    
@admin.register(Covid)
class CovidInline(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'primera_seccion_titulo_imagen',
                'primera_seccion_alt_imagen',
                'primera_seccion_imagen',
                'primera_seccion_video_url',
                'primera_seccion_titulo',
                'primera_seccion_fecha',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                )
        }),
    )
    
    
    inlines = [CovidComunicadoInline]