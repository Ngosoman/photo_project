from django.urls import path
from . import views

urlpatterns = [
    # AUTH
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),

    # GALLERY
    path('', views.gallery_home, name='gallery_home'),
    path('upload/', views.upload_photo, name='upload_photo'),
]
