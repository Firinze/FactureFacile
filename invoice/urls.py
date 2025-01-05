from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

import facture
from invoice import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('facture.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
