from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from photo_gallery import views


urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # Gallery
    path("", views.gallery_home, name="gallery_home"),
    path("upload/", views.upload_photo, name="upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
