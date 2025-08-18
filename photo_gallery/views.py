from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm
from .forms import PhotoUploadForm

def gallery_home(request):
    return render(request, 'gallery_home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            return redirect('gallery_home')
    else:
        form = PhotoUploadForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def gallery_home(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery_home.html', {'photos': photos})
from django.urls import path
from . import views
from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")

def gallery_home(request):
    return render(request, "gallery.html")
