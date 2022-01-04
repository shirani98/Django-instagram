from django.db.models.fields import SlugField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from post.forms import AddPostForm
from .models import Post 
# Create your views here.
class PostList(ListView):
    model = Post
    template_name = "post/index.html"

    
class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail.html'
