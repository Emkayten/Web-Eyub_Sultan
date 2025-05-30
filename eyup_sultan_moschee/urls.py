from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hauptseite.urls')),
    path('fuehrung/', include('fuehrung.urls')),
    path('gemeinde/', include('gemeinde.urls')),
    path('mitgliedsantrag/', include('mitgliedsantrag.urls')),
    path('downloads/', include('downloads.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
