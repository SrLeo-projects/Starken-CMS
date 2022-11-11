from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

from cms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('faicon/', include('faicon.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)