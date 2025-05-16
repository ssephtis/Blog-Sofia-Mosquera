from django.contrib import admin
from django.urls import path, include
from pages.views import about_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página de "Acerca de mí"
    path('about/', about_view, name='about'),

    # Autenticación y perfil
    path('accounts/', include('accounts.urls')),

    # CKEditor para texto enriquecido
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Sistema de mensajería
    path('messages/', include('messenger.urls')),

    # Blog principal (inicio, create, detalle, etc.)
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)