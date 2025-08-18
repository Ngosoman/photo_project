from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    path('upload/', views.upload_photo, name='upload_photo'),

]