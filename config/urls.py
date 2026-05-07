from baton.autodiscover import admin
from django.urls import path, include

# 👇 IMPORTANTE
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', include('adminpanel.urls')),
]

# 👇 ESTO ES LO QUE TE FALTABA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)