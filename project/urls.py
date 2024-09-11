from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "ECOMMERCE"
admin.site.site_title = "ARK ADMIN"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ecomapp.urls',namespace='ecomapp')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)