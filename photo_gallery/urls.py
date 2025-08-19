from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Gallery
    path('', views.gallery_home, name='gallery_home'),  
    path('upload/', views.upload_photo, name='upload_photo'),
]
