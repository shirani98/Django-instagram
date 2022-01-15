from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from comment.models import Comment
from django.shortcuts import redirect
from .models import Post 
from comment.forms import AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from accounts.models import MyUser
from like.models import Like
import redis
from django.conf import settings
from django.shortcuts import get_object_or_404
class PostList(ListView):
    model = Post
    template_name = "post/feed.html"

 
    
redis_con = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB)       
class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comments'] = Comment.objects.filter(post = post, is_reply = False)
        context['form'] = AddCommentForm()
        context['form_reply'] = AddCommentForm()
        context['post_view'] =redis_con.incr( self.object.id )
        if self.request.user.is_authenticated:
            context['is_like'] = Like.objects.filter(post = post , user = self.request.user).exists()
        return context
    
    def post(self, *args, **kwargs):
        body = self.request.POST.get('body')
        postslug = self.kwargs.get('slug')
        post = Post.objects.get(slug=postslug)
        Comment.objects.create(body=body,user= self.request.user,post = post)
        return redirect('post:detail',post.slug)
class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('body','image')
    template_name = 'post/addpost.html'
    def get_success_url(self, **kwargs):         
        return reverse_lazy('accounts:profile', kwargs = {'user': self.request.user})
    def form_valid(self,form):
        new_post = form.save(commit=False)
        new_post.user = self.request.user
        new_post.save()
        return super().form_valid(form)
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    def get_success_url(self, **kwargs):         
        return reverse_lazy('accounts:profile', kwargs = {'user': self.request.user})
    
    def get(self,request, *args, **kwargs):
        post = Post.objects.get(slug = self.kwargs['slug'])
        if post.user == request.user :
            return self.delete(request, *args, **kwargs)
        else:
            raise Http404
class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post/addpost.html'