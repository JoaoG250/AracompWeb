from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf.urls.static import static  # Not for production

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('enigmas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Not for production
