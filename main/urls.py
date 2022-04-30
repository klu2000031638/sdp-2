from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from . import settings

urlpatterns = [
path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
path('admin/', admin.site.urls),
path('', include('pages.urls')), 
path('', include('store.urls')),

# User management
path('accounts/', include('allauth.urls')), # new
# Local apps
path('accounts/', include('users.urls')),
path('services/', include('services.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
