from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('encyclopedia.urls')),
    path('i18n/', include('django.conf.urls.i18n')),  # <-- Добавить этот маршрут
]

if settings.USE_I18N:
    urlpatterns += i18n_patterns(
        path('', include('encyclopedia.urls')),  # <-- Перенес админку вниз
        path('admin/', admin.site.urls),
    )
