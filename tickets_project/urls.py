from os import stat
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secret/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('tickets.urls')),
    path('editor/', include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)