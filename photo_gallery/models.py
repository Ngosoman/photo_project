
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=200, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    likes = models.ManyToManyField(User, related_name="liked_photos", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title