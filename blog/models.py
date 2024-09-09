from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post_detail/{self.id}/'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.URLField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.user.username} Profile'