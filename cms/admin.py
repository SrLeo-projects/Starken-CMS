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
                'primera_seccion_boton_principal',
                'primera_seccion_boton_principal_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
                ('primera_seccion_titulo_imagen', 'primera_seccion_alt_imagen'),
                'primera_seccion_imagen',
                'primera_seccion_subtitulo',
                'primera_seccion_subtitulo_descripcion',
                'primera_seccion_link', 
                'primera_seccion_link_texto',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
                'segunda_seccion_boton_principal',
                'segunda_seccion_boton_principal_url',
                'segunda_seccion_boton_secundario',
                'segunda_seccion_boton_secundario_url',
                'servicios',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                ('tercera_seccion_titulo', 'tercera_seccion_destacado'),
                'tercera_seccion_descripcion',
                'tercera_seccion_boton_principal',
                'tercera_seccion_boton_principal_url',
                'tercera_seccion_boton_secundario',
                'tercera_seccion_boton_secundario_url',
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
                ('quinta_seccion_app_store_url', 'quinta_seccion_google_play_url'),
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
                'primera_seccion_boton_principal',
                'primera_seccion_boton_principal_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'tercera_seccion_boton_principal',
                'tercera_seccion_boton_principal_url',
                'tercera_seccion_boton_secundario',
                'tercera_seccion_boton_secundario_url',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                ('cuarta_seccion_titulo', 'cuarta_seccion_destacado'),
                'cuarta_seccion_descripcion',
                'cuarta_seccion_boton_principal',
                'cuarta_seccion_boton_principal_url',
                'cuarta_seccion_boton_secundario',
                'cuarta_seccion_boton_secundario_url',
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
                'quinta_seccion_boton_principal',
                'quinta_seccion_boton_principal_url',
                'quinta_seccion_boton_secundario',
                'quinta_seccion_boton_secundario_url',
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
                'primera_seccion_primer_titulo',
                'primera_seccion_primera_descripcion',
                'primera_seccion_segundo_titulo',
                'primera_seccion_segunda_descripcion',
                'primera_seccion_boton_principal',
                'primera_seccion_boton_principal_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
                
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
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                'cuarta_seccion_subtitulo',
                'cuarta_seccion_titulo',
                'cuarta_seccion_destacado',
                'cuarta_seccion_descripcion',
                'cuarta_seccion_titulo_imagen',
                'cuarta_seccion_alt_imagen',
                'cuarta_seccion_imagen',
                'cuarta_seccion_video',
            )
        }),
    )

    inlines = [StarkenProBeneficioInline, StarkenProPasoInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Tercera Sección", "Beneficios", "Cuarta Sección", "Indicaciones")
    

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
                'primera_seccion_boton_principal',
                'primera_seccion_boton_principal_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                ('segunda_seccion_titulo', 'segunda_seccion_destacado'),
                'segunda_seccion_descripcion',
                'segunda_seccion_boton_principal',
                'segunda_seccion_boton_principal_url',
                'segunda_seccion_boton_secundario',
                'segunda_seccion_boton_secundario_url',
                'segunda_seccion_preguntas',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                ('tercera_seccion_titulo_imagen', 'tercera_seccion_alt_imagen'),
                'tercera_seccion_imagen',
                'formulario_titulo',
                'formulario_subtitulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_nombre', 
                'etiqueta_email',
                'etiqueta_orden_de_flete',
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
            'fields': ('titulo_categoria', 'primera_seccion_ocultar', 'descripcion', 'imagen')
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
                'tercera_seccion_icono_primer_bloque',
                'tercera_seccion_titulo_primer_bloque',
                'tercera_seccion_descripcion_primer_bloque',
                'tercera_seccion_url_primer_bloque',
                'tercera_seccion_icono_segundo_bloque',
                'tercera_seccion_titulo_segundo_bloque',
                'tercera_seccion_descripcion_segundo_bloque',
                'tercera_seccion_url_segundo_bloque'
            )
        }),
    )
    

class RedSocialInline(admin.StackedInline):
    model = RedSocial
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
                'primera_seccion_titulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton_principal',
                'primera_seccion_boton_principal_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_icon_whatsapp',
                'segunda_seccion_url_whatsapp',
                'segunda_seccion_titulo_whatsapp',
                'segunda_seccion_descripcion_whatsapp',
                'segunda_seccion_icon_telefono',
                'segunda_seccion_titulo_telefono', 
                'segunda_seccion_descripcion_telefono', 
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
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
    )
    
    inlines = [RedSocialInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Redes Sociales", "Tercera Sección", "Cuarta Sección")
    
    
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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'cuarta_seccion_boton_secundario',
                'cuarta_seccion_boton_secundario_url',
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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'etiqueta_rut_empresa',
                'etiqueta_nombre_contacto',
                'etiqueta_razon_social',
                'etiqueta_rut_contacto',
                'etiqueta_direccion',
                'etiqueta_email_contacto',
                'etiqueta_comuna',  
                'etiqueta_telefono_contacto', 
                'etiqueta_rubro',
                'etiqueta_comentario',
                'tercera_seccion_titulo_imagen',
                'tercera_seccion_alt_imagen',
                'tercera_seccion_imagen',
                'tercera_seccion_titulo',
                'tercera_seccion_descripcion',
                'tercera_seccion_enlace',
                'tercera_seccion_enlace_url',
                'tercera_seccion_titulo_carrusel',
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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'cuarta_seccion_boton_secundario',
                'cuarta_seccion_boton_secundario_url',
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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'tercera_seccion_boton_secundario',
                'tercera_seccion_boton_secundario_url',
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
                'cuarta_seccion_boton_secundario',
                'cuarta_seccion_boton_secundario_url',
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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'etiqueta_tipo_de_cliente',
                'etiqueta_rut',
                'etiqueta_nombre', 
                'etiqueta_email',  
                'etiqueta_telefono',
                'etiqueta_fecha_de_nacimiento', 
                'etiqueta_direccion',
                'etiqueta_comuna',
                'etiqueta_rubro',
                'etiqueta_envios_mensuales',
                'etiqueta_producto',
                'etiqueta_url_facebook',
                'etiqueta_url_instagram',
                'etiqueta_dls_cajero',
                'tercera_seccion_titulo_imagen',
                'tercera_seccion_alt_imagen',
                'tercera_seccion_imagen',
                'tercera_seccion_titulo_derecho',
                'tercera_seccion_destacado_derecho',
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                'cuarta_seccion_ocultar',
                'zona_partner_seccion_titulo_logo',
                'zona_partner_seccion_alt_logo',
                'zona_partner_seccion_logo',
                'zona_partner_seccion_descripcion',
                'zona_partner_seccion_titulo_imagen',
                'zona_partner_seccion_alt_imagen',
                'zona_partner_seccion_imagen',
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'quinta_seccion_ocultar',
                'quinta_seccion_titulo',
                'quinta_seccion_destacado',
                'quinta_seccion_titulo_imagen',
                'quinta_seccion_alt_imagen',
                'quinta_seccion_imagen',
                'quinta_seccion_video',
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
    
    inlines = [MypymesBeneficiosInline,]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Beneficios", "Tercera Sección", "Zona Partner", "Cuarta Sección", "Quinta Sección", "Sexta Sección", "Séptima Sección")
    
    

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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'formulario_primer_titulo',
                'formulario_segundo_titulo',
                'formulario_boton_principal',
                'etiqueta_tipo_reclamo',
                'valor_orden_de_flete',
                'valor_atencion_al_cliente',
                'etiqueta_numero_orden_de_flete',
                'etiqueta_inconveniente',
                'etiqueta_tipo_cliente',
                'valor_destinatario',
                'valor_remitente',
                'etiqueta_rut', 
                'etiqueta_nombre',
                'etiqueta_apellido_paterno',
                'etiqueta_apellido_materno',
                'etiqueta_telefono_fijo',
                'etiqueta_telefono_celular',
                'etiqueta_email',
                'etiqueta_direccion',  
                'etiqueta_reclamo',
                'primera_notificacion',
                'mensaje',
                'segunda_notificacion',
                
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
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'cuarta_seccion_boton_principal',
                'cuarta_seccion_boton_principal_enlace',
                'cuarta_seccion_boton_secundario',
                'cuarta_seccion_boton_secundario_enlace',
                
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
                'primera_seccion_titulo',
                'primera_seccion_subtitulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
                )
        }),
    )
    
    
    inlines = [CovidComunicadoInline]
    


@admin.register(FormularioEmpresa)
class FormularioEmpresaAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['rut_empresa', 'nombre_contacto', 'rut_contacto', 'razon_social', 'comuna', 'rubro', 'email', 'direccion', 'telefono' ]
    search_fields = ['nombre_contacto', 'comuna', 'rubro', 'razon_social']
    list_filter = ['nombre_contacto', 'comuna', 'rubro']
    fieldsets = (
        ('Formulario', {
            'fields': ('rut_empresa', 'rut_contacto', 'nombre_contacto','razon_social', 'direccion', 'email', 'telefono', 'comuna', 'rubro', 'comentario',)
        }),
    )
    
@admin.register(FormularioMypymes)
class FormularioMypymesAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['tipo', 'nombre', 'rut', 'comuna', 'rubro', 'email', 'direccion', 'telefono', 'fecha_nacimiento' ]
    search_fields = ['nombre_contacto', 'comuna', 'rubro', 'tipo', 'dls_cajero']
    list_filter = ['nombre', 'comuna', 'rubro']
    fieldsets = (
        ('Formulario', {
            'fields': ('tipo', 'rut', 'nombre', 'email', 'telefono', 'fecha_nacimiento', 'direccion', 'comuna', 'rubro', 'envios_mensuales', 'producto', 'url_facebook', 'url_instagram', 'dls_cajero',)
        }),
    )
    

class ServiciosCarruselInline(admin.StackedInline):
    model = ServiciosCarrusel
    extra = 0

@admin.register(Servicios)
class ServiciosAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    filter_horizontal = ['segunda_seccion_servicios']
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
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
                'segunda_seccion_servicios',
                
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_titulo_imagen',
                'tercera_seccion_alt_imagen',
                'tercera_seccion_imagen',
                'tercera_seccion_titulo',
                'tercera_seccion_descripcion',
                'tercera_seccion_primer_boton',
                'tercera_seccion_primer_boton_url',
                'tercera_seccion_segundo_boton',
                'tercera_seccion_segundo_boton_url',
                
            )
        }),
       
    )
    
    inlines = [ServiciosCarruselInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Tercera Sección", "Imágenes")


class RegistroBeneficiosInline(admin.StackedInline):
    model = RegistroBeneficios
    extra = 0

@admin.register(Registro)
class RegistroAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_rut',
                'etiqueta_nombre',
                'etiqueta_apellido',
                'etiqueta_email',
                'etiqueta_direccion',
                'etiqueta_comuna',
                'etiqueta_sucursal',
                'etiqueta_telefono',
                'etiqueta_movil',
                'etiqueta_contraseña',
                'primera_seccion_titulo',
                'primera_seccion_subtitulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
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
       
    )
    
    inlines = [RegistroBeneficiosInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Beneficios-Registro", "Cuarta Sección")
    


class LoginBeneficiosInline(admin.StackedInline):
    model = LoginBeneficios
    extra = 0

@admin.register(Login)
class LoginAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ['titulo', 'descripcion']
    fieldsets = (
        ('General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Primera Sección', {
            'fields': (
                'primera_seccion_ocultar',
                'formulario_titulo',
                'formulario_descripcion',
                'formulario_boton_principal',
                'etiqueta_usuario', 
                'etiqueta_contraseña',
                'primera_seccion_titulo',
                'primera_seccion_subtitulo',
                'primera_seccion_descripcion',
                'primera_seccion_boton',
                'primera_seccion_boton_url',
                'primera_seccion_boton_secundario',
                'primera_seccion_boton_secundario_url',
            )
        }),
        ('Segunda Sección', {
            'fields': (
                'segunda_seccion_ocultar',
                'segunda_seccion_titulo',
                'segunda_seccion_destacado',
                'segunda_seccion_descripcion',
                'segunda_seccion_boton',
                'segunda_seccion_boton_url',
                'segunda_seccion_boton_secundario',
                'segunda_seccion_boton_secundario_url',
                'segunda_seccion_titulo_imagen',
                'segunda_seccion_alt_imagen',
                'segunda_seccion_imagen',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                'tercera_seccion_ocultar',
                'tercera_seccion_titulo',
                'tercera_seccion_destacado',
                'tercera_seccion_subtitulo',
                
            )
        }),
    )
    
    inlines = [LoginBeneficiosInline]
    jazzmin_section_order = ("General", "Primera Sección", "Segunda Sección", "Tercera Sección", "Beneficios-Login")