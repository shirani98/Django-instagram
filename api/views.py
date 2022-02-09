from django.shortcuts import render
from rest_framework import generics
from post.models import Post
from .serializers import PostSerializers

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers