from django.db.models.fields import SlugField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.urls.base import reverse
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from comment.models import Comment
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from post.forms import AddCommentForm, AddPostForm
from .models import Post 
# Create your views here.
class PostList(ListView):
    model = Post
    template_name = "post/index.html"

    
class PostDetail(DetailView, View):
    model = Post
    template_name = 'post/detail.html'
    form_class = AddCommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post = self.object)
        context['form'] = AddCommentForm()
        return context
    
    def post(self, *args, **kwargs):
        body = self.request.POST.get('body')
        postslug = self.kwargs.get('slug')
        post = Post.objects.get(slug=postslug)
        Comment.objects.create(body=body,user= self.request.user,post = post)
        url_match = reverse_lazy('post:detail', kwargs = {'slug': post.slug, 'year' : post.created.year, 'month' : post.created.month, 'day' : post.created.day})
        return redirect(url_match)              
