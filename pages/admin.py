from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from tabular_export.admin import export_to_csv_action, export_to_excel_action
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
class PageAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'descripcion')

    inlines = [
        PageDetailInline,
    ]

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.0.min.js', 'js/dynamic_field_selector.js')


@admin.register(BannerSeccion)
class BannerSeccionAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'subtitulo', 'descripcion')
    
@admin.register(Beneficio)
class BeneficioAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'descripcion')

@admin.register(BeneficioSeccion)
class BeneficioSeccionAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'descripcion')
    filter_horizontal = ['beneficios']

@admin.register(BasicoSeccion)
class BasicoSeccionAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'subtitulo', 'descripcion')

@admin.register(Servicio)
class ServicioAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'descripcion')

@admin.register(ServiciosSeccion)
class ServiciosSeccionAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'descripcion')
    filter_horizontal = ['servicios']

    
@admin.register(Bloques)
class BloquesAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('titulo', 'descripcion')

@admin.register(BloquesSeccion)
class BloquesSeccionAdmin(ImportExportModelAdmin):
    actions = (export_to_excel_action, export_to_csv_action)
    list_display = ('pagina',)
    filter_horizontal = ['bloques']