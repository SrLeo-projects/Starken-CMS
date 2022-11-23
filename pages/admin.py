from django.contrib import admin

from pages.models import *

class PageDetailInline(admin.StackedInline):
    model = PageDetail
    extra = 0

    # add classname to type field
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(PageDetailInline, self).get_formset(request, obj, **kwargs)
        formset.form.base_fields['type'].widget.attrs['class'] = 'page_detail_type'
        return formset

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')

    inlines = [
        PageDetailInline,
    ]

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.0.min.js', 'js/dynamic_field_selector.js')

@admin.register(BasicSeccion)
class BasicSeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'descripcion')

@admin.register(VideoSeccion)
class VideoSeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'descripcion', 'url')

class benefitInline(admin.StackedInline):
    model = Benefit
    extra = 0

@admin.register(BenefitSeccion)
class BenefitSeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')

    inlines = [
        benefitInline,
    ]

@admin.register(BannerSeccion)
class BannerSeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'descripcion')
    

@admin.register(FormularioSeccion)
class FormularioSeccionAdmin(admin.ModelAdmin):
    list_display = ('primer_titulo', 'primera_descripcion')
    filter_horizontal = ['etiqueta']

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('etiqueta',)
    
@admin.register(BloquesSeccion)
class BloquesSeccionAdmin(admin.ModelAdmin):
    list_display = ('primer_bloque_titulo', 'segundo_bloque_titulo')