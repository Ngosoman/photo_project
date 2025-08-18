"""
URL configuration for photo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register.html'),
    path('accounts/', include('accounts.urls')),
    path('', include('photo_gallery.urls')),  # gallery homepage
    path("admin/", admin.site.urls),

    # Accounts routes
    path("accounts/", include("accounts.urls")),

    # Dashboard route
    path("dashboard/", account_views.dashboard, name="dashboard"),

    # Gallery home
    path("gallery_home/", account_views.gallery_home, name="gallery_home"),
    # Authentication routes
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    # Photo upload route
    # path('upload/', views.upload_photo, name='upload_photo'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # authentication routes
    path('', include('photo_gallery.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)