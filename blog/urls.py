from django.urls import path

from blog.views import HomeView, PostDetailView, PostCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post_detail/<int:pk>/',
         PostDetailView.as_view(),
         name='post_detail'),
    path('post_create/',
         PostCreateView.as_view(),
         name='post_create'),
]
