from django.contrib import admin

from cms.models import *

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'button', 'button_url')
    list_filter = ('title', 'description', 'image', 'button', 'button_url')

class BannerInline(admin.StackedInline):
    model = Banner
    extra = 0

class OptionInline(admin.StackedInline):
    model = Option
    extra = 0

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    
    filter_horizontal = ['services']

    fieldsets = (
        ('General', {
            'fields': ('title', 'description')
        }),
        ('Primera Sección', {
            'fields': (
                ('first_section_title', 'first_section_highlight'),
                'first_section_description',
                ('first_section_main_button', 'first_section_main_button_url'),
                ('first_section_secondary_button', 'first_section_secondary_button_url'),
                'first_section_image',
                ('first_section_subtitle', 'first_section_subtitle_description'),
                ('first_section_link', 'first_section_link_text'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('second_section_title', 'second_section_highlight'),
                'second_section_description',
                ('second_section_main_button', 'second_section_main_button_url'),
                'services',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                ('third_section_title', 'third_section_highlight'),
                'third_section_description',
                ('third_section_main_button', 'third_section_main_button_url'),
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                ('fourth_section_card_1_image', 'fourth_section_card_2_image'),
                ('fourth_section_card_1_title', 'fourth_section_card_2_title'),
                ('fourth_section_card_1_description', 'fourth_section_card_2_description'),
                ('fourth_section_card_1_button', 'fourth_section_card_2_button'),
                ('fourth_section_card_1_button_url', 'fourth_section_card_2_button_url'),
            )
        }),
        ('Quinta Sección', {
            'fields': (
                ('fifth_section_title', 'fifth_section_words'),
                'fifth_section_description',
                ('fifth_section_main_button', 'fifth_section_main_button_url'),
            )
        }),
    )

    inlines = [BannerInline, OptionInline]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    fieldsets = (
        ('General', {
            'fields': ('title', 'description')
        }),
        ('Primera Sección', {
            'fields': (
                ('first_section_image', 'first_section_title'),
                'first_section_description',
                ('first_section_main_button', 'first_section_main_button_url'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('second_section_title', 'second_section_highlight'),
                'second_section_description',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                ('third_section_title', 'third_section_highlight'),
                'third_section_description',
                ('third_section_main_button', 'third_section_main_button_url'),
            )
        }),
        ('Cuarta Sección', {
            'fields': (
                ('fourth_section_title', 'fourth_section_highlight'),
                'fourth_section_description',
                ('fourth_section_main_button', 'fourth_section_main_button_url'),
            )
        }),
        ('Quinta Sección', {
            'fields': (
                'fifth_section_image',
                ('fifth_section_title', 'fifth_section_highlight'),
                'fifth_section_subtitle',
                'fifth_section_description',
                ('fifth_section_main_button', 'fifth_section_main_button_url'),
            )
        }),
    )

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'created_at']
    search_fields = ['title']
    list_filter = ['type']
    
class StarkenProBenefitInline(admin.StackedInline):
    model = StarkenProBenefit
    extra = 0

class StarkenProStepInline(admin.StackedInline):
    model = StarkenProStep
    extra = 0

@admin.register(StarkenPro)
class StarkenProAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    fieldsets = (
        ('General', {
            'fields': ('title', 'description')
        }),
        ('Primera Sección', {
            'fields': (
                'first_section_image',
                ('first_section_title', 'first_section_highlight'),
                'first_section_description',
                ('first_section_main_button', 'first_section_main_button_url'),
                'first_section_message',
            )
        }),
        ('Formulario', {
            'fields': (
                'form_title',
                'form_description',
                'form_main_button',
            )
        }),
        ('Labels', {
            'fields': (
                ('label_name', 'label_email', 'label_message'),
            )
        }),
        ('Segunda Sección', {
            'fields': (
                ('second_section_title', 'second_section_highlight'),
                'second_section_description',
            )
        }),
        ('Tercera Sección', {
            'fields': (
                ('third_section_title', 'third_section_highlight'),
            )
        }),
    )

    inlines = [StarkenProBenefitInline, StarkenProStepInline]