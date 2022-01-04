from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Comment
from django.urls import reverse
from post.forms import AddCommentForm
# Create your views here.
class CommentCreate(CreateView):
    model = Comment
    form_class = AddCommentForm
    def get_success_URL(self):
        return reverse ('accounts:dash')
