from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'post_create.html'
