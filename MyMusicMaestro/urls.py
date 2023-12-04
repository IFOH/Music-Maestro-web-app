from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('albums/', include('app_album_viewer.urls')),
    path('', include('app_pages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
