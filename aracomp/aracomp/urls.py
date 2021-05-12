from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

# from django.conf import settings # Not for production
# from django.conf.urls.static import static # Not for production

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Not for production
