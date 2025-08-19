from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views
from gallery import views as gallery_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts app (login/register/logout)
    path('accounts/', include('accounts.urls')),

    # Gallery app (home, upload, etc.)
    path('gallery/', include('gallery.urls')),

    # Dashboard
    path('dashboard/', account_views.dashboard, name='dashboard'),

    # Default homepage -> gallery
    path('', gallery_views.gallery_home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
