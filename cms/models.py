from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='título')
    description = models.TextField(blank=True, verbose_name='descripción')

    class Meta:
        abstract = True

class Service(BaseModel):
    image = models.ImageField(upload_to='services', verbose_name='imagen')
    button = models.CharField(max_length=255, verbose_name='botón')
    button_url = models.URLField(verbose_name='url del botón')

    class Meta:
        verbose_name = 'servicio'

class Home(BaseModel):
    first_section_title = models.CharField(max_length=255, verbose_name='título')
    first_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    first_section_description = models.TextField(blank=True, verbose_name='descripción')
    
    first_section_main_button = models.CharField(max_length=255, verbose_name='botón principal')
    first_section_main_button_url = models.URLField(verbose_name='url del botón principal')

    first_section_secondary_button = models.CharField(max_length=255, verbose_name='botón secundario')
    first_section_secondary_button_url = models.URLField(verbose_name='url del botón secundario')

    first_section_image = models.ImageField(upload_to='home', verbose_name='imagen')
    first_section_subtitle = models.CharField(max_length=255, verbose_name='subtítulo')
    first_section_subtitle_description = models.TextField(blank=True, verbose_name='descripción')

    first_section_link = models.URLField(verbose_name='enlace')
    first_section_link_text = models.CharField(max_length=255, verbose_name='texto del enlace')

    second_section_title = models.CharField(max_length=255, verbose_name='título')
    second_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    second_section_description = models.TextField(blank=True, verbose_name='descripción')

    second_section_main_button = models.CharField(max_length=255, verbose_name='botón principal')
    second_section_main_button_url = models.URLField(verbose_name='url del botón principal')

    third_section_title = models.CharField(max_length=255, verbose_name='título')
    third_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    third_section_description = models.TextField(blank=True, verbose_name='descripción')

    third_section_main_button = models.CharField(max_length=255, verbose_name='botón principal')
    third_section_main_button_url = models.URLField(verbose_name='url del botón principal')

    fourth_section_card_1_image = models.ImageField(upload_to='home', verbose_name='imagen')
    fourth_section_card_1_title = models.CharField(max_length=255, verbose_name='título')
    fourth_section_card_1_description = models.TextField(blank=True, verbose_name='descripción')
    fourth_section_card_1_button = models.CharField(max_length=255, verbose_name='botón')
    fourth_section_card_1_button_url = models.URLField(verbose_name='url del botón')

    fourth_section_card_2_image = models.ImageField(upload_to='home', verbose_name='imagen')
    fourth_section_card_2_title = models.CharField(max_length=255, verbose_name='título')
    fourth_section_card_2_description = models.TextField(blank=True, verbose_name='descripción')
    fourth_section_card_2_button = models.CharField(max_length=255, verbose_name='botón')
    fourth_section_card_2_button_url = models.URLField(verbose_name='url del botón')

    fifth_section_title = models.CharField(max_length=255, verbose_name='título')
    fifth_section_words = models.CharField(max_length=255, verbose_name='palabras', help_text='separadas por coma')
    fifth_section_description = models.TextField(blank=True, verbose_name='descripción')

    fifth_section_main_button = models.CharField(max_length=255, verbose_name='botón')
    fifth_section_main_button_url = models.URLField(verbose_name='url del botón')

    services = models.ManyToManyField(Service, verbose_name='servicios')

    class Meta:
        verbose_name_plural = 'home'
    
    def __str__(self):
        return self.title
    
    def get_highlighted_title(self, section):
        return self.__dict__[f'{section}_section_title'].replace(self.__dict__[f'{section}_section_highlight'], f'<strong class="fw-bold text-primary">{self.__dict__[f"{section}_section_highlight"]}</strong>')

# Banner -> HomeBanner
class Banner(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='carousel')

    image = models.ImageField(upload_to='carousel', verbose_name='imagen')
    subtitle = models.CharField(max_length=255, verbose_name='subtítulo')

    button = models.CharField(max_length=255, verbose_name='botón')
    button_url = models.URLField(verbose_name='url del botón')

    short_title = models.CharField(max_length=255, verbose_name='título corto')
    short_description = models.CharField(max_length=255, verbose_name='descripción corta')

    def __str__(self):
        return self.title

# Option -> HomeOption
class Option(BaseModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='options')

    image = models.ImageField(upload_to='options', verbose_name='imagen')

    button = models.CharField(max_length=255, verbose_name='botón')
    button_url = models.URLField(verbose_name='url del botón')

    class Meta:
        verbose_name = 'opción'
        verbose_name_plural = 'opciones'

    def __str__(self):
        return self.title

# SOMOS STARKEN

class About(BaseModel):
    first_section_image = models.ImageField(upload_to='about', verbose_name='imagen')
    first_section_title = models.CharField(max_length=255, verbose_name='título')
    first_section_description = models.TextField(blank=True, verbose_name='descripción')
    first_section_main_button = models.CharField(max_length=255, verbose_name='botón')
    first_section_main_button_url = models.URLField(verbose_name='url del botón')

    second_section_title = models.CharField(max_length=255, verbose_name='título')
    second_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    second_section_description = models.TextField(blank=True, verbose_name='descripción')

    third_section_title = models.CharField(max_length=255, verbose_name='título')
    third_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    third_section_description = models.TextField(blank=True, verbose_name='descripción')
    third_section_main_button = models.CharField(max_length=255, verbose_name='botón')
    third_section_main_button_url = models.URLField(verbose_name='url del botón')
    
    fourth_section_title = models.CharField(max_length=255, verbose_name='título')
    fourth_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    fourth_section_description = models.TextField(blank=True, verbose_name='descripción')
    fourth_section_main_button = models.CharField(max_length=255, verbose_name='botón')
    fourth_section_main_button_url = models.URLField(verbose_name='url del botón')

    fifth_section_image = models.ImageField(upload_to='about', verbose_name='imagen')
    fifth_section_title = models.CharField(max_length=255, verbose_name='título')
    fifth_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    fifth_section_subtitle = models.CharField(max_length=255, verbose_name='subtítulo')
    fifth_section_description = models.TextField(blank=True, verbose_name='descripción')
    fifth_section_main_button = models.CharField(max_length=255, verbose_name='botón')
    fifth_section_main_button_url = models.URLField(verbose_name='url del botón')

    class Meta:
        verbose_name = 'somos STARKEN'
        verbose_name_plural = 'somos STARKEN'
    
    def __str__(self):
        return self.title

# Agregar más campos en base a https://desa.sbmundo.com/starken/responsabilidad-social.html
# TODO revisar campos de artículos
class Article(BaseModel):
    class Type(models.TextChoices):
        NOTICIA = 'noticia', 'Noticia'
        RESPONSABILIDAD_SOCIAL = 'responsabilidad social', 'Responsabilidad social'
        SUSTENTABILIDAD = 'sustentabilidad', 'Sustentabilidad'

    image = models.ImageField(upload_to='articles', verbose_name='imagen')
    title = models.CharField(max_length=255, verbose_name='título')
    content = RichTextUploadingField(verbose_name='contenido')
    type = models.CharField(max_length=255, choices=Type.choices, verbose_name='tipo')

    created_at = models.DateField(verbose_name='fecha de creación')
    updated_at = models.DateField(verbose_name='fecha de actualización')

    class Meta:
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
    
    def __str__(self):
        return self.title

# Starken PRO
class StarkenPro(BaseModel):
    first_section_image = models.ImageField(upload_to='starkenpro', verbose_name='imagen')
    first_section_title = models.CharField(max_length=255, verbose_name='título')
    first_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    first_section_description = models.TextField(blank=True, verbose_name='descripción')
    first_section_main_button = models.CharField(max_length=255, verbose_name='botón')
    first_section_main_button_url = models.URLField(verbose_name='url del botón')
    first_section_message = models.CharField(max_length=255, verbose_name='mensaje')

    form_title = models.CharField(max_length=255, verbose_name='título')
    form_description = models.TextField(blank=True, verbose_name='descripción')
    form_main_button = models.CharField(max_length=255, verbose_name='botón')
    label_name = models.CharField(max_length=255, verbose_name='nombre')
    label_email = models.CharField(max_length=255, verbose_name='email')
    label_message = models.CharField(max_length=255, verbose_name='mensaje')

    second_section_title = models.CharField(max_length=255, verbose_name='título')
    second_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    second_section_description = models.TextField(blank=True, verbose_name='descripción')

    third_section_title = models.CharField(max_length=255, verbose_name='título')
    third_section_highlight = models.CharField(max_length=255, verbose_name='destacado')

    class Meta:
        verbose_name = 'starken PRO'
        verbose_name_plural = 'starken PRO'
    
    def __str__(self):
        return self.title

class StarkenProBenefit(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO')
    image = models.ImageField(upload_to='starkenpro', verbose_name='imagen')

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    def __str__(self):
        return self.title

class StarkenProStep(BaseModel):
    starken_pro = models.ForeignKey(StarkenPro, on_delete=models.CASCADE, verbose_name='starken PRO')

    class Meta:
        verbose_name = 'paso'
        verbose_name_plural = 'pasos'
    
    def __str__(self):
        return self.title
    
#Help Center
class HelpCenter(BaseModel):
    form_title_contact = models.CharField(max_length=255, verbose_name='título_contact')
    form_description_contact = models.TextField(blank=True, verbose_name='descripción_contact')
    form_main_button_contact = models.CharField(max_length=255, verbose_name='botón_contact')
    label_name_contact = models.CharField(max_length=255, verbose_name='nombre_contact')
    label_email_contact = models.CharField(max_length=255, verbose_name='email_contact')
    label_phone_contact = models.CharField(max_length=255, verbose_name='phone_contact')
    label_business_type_contact = models.CharField(max_length=255, verbose_name='business_type_contact')
    label_message_contact = models.CharField(max_length=255, verbose_name='mensaje_contact')
    second_section_title = models.CharField(max_length=255, verbose_name='título')
    second_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    second_section_description = models.TextField(blank=True, verbose_name='descripción')
    
    third_section_title = models.CharField(max_length=255, verbose_name='título')
    third_section_highlight = models.CharField(max_length=255, verbose_name='destacado')
    third_section_description = models.TextField(blank=True, verbose_name='descripción')
    third_section_main_button = models.CharField(max_length=255, verbose_name='botón')
    third_section_main_button_url = models.URLField(verbose_name='url del botón')
    
    form_title = models.CharField(max_length=255, verbose_name='título')
    form_description = models.TextField(blank=True, verbose_name='descripción')
    form_main_button = models.CharField(max_length=255, verbose_name='botón')
    label_name = models.CharField(max_length=255, verbose_name='nombre')
    label_email = models.CharField(max_length=255, verbose_name='email')
    label_message = models.CharField(max_length=255, verbose_name='mensaje')
    fourth_section_image = models.ImageField(upload_to='helpcenter', verbose_name='imagen')
    
    class Meta:
        verbose_name = 'centro de ayuda'
        verbose_name_plural = 'centros de ayuda'
        
class HelpCenterQuestion(BaseModel):
    help_center = models.ForeignKey(HelpCenter, on_delete=models.CASCADE, verbose_name='Help Center')
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    
class HelpCenterBenefit(BaseModel):
    help_center = models.ForeignKey(HelpCenter, on_delete=models.CASCADE, verbose_name='Help Center')
    image = models.ImageField(upload_to='help_center', verbose_name='imagen')

    class Meta:
        verbose_name = 'beneficio'
        verbose_name_plural = 'beneficios'
    
    def __str__(self):
        return self.title

#Condiciones de Servicio
class TermsofService(BaseModel):
    class Meta:
        verbose_name = 'Condición de Servicio'
        verbose_name_plural = 'Condiciones de Servicio'

class TermsofServicePoint(BaseModel):
    terms_of_service = models.ForeignKey(TermsofService, on_delete=models.CASCADE, verbose_name='Terms of Service')
    class Meta:
        verbose_name = 'Punto de Condición de Servicio'
        verbose_name_plural = 'Puntos de Condiciones de Servicio'