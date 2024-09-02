from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import CreateForm
from blog.models import Post, Category


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
    form_class = CreateForm
    template_name = 'post_create.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = CreateForm
    template_name = 'post_update.html'

    def get_success_url(self):
        return f'/post_detail/{self.object.id}/'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse_lazy('home')


def create_post(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'post_create_function.html',
                      {'categories': categories})
    title = request.POST.get('title')
    content = request.POST.get('content')
    category_id = request.POST.get('category_id')
    category = Category.objects.get(id=category_id)
    author_id = request.POST.get('author_id')
    author = User.objects.get(id=author_id)
    Post.objects.create(title=title, content=content, category=category,
                        author=author)
    return render(request, 'post_create_function.html')


def likes_or_not(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return render(request,
                      'post_detail.html',
                      {'object': post})

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
