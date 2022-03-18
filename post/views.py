from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from comment.models import Comment
from django.shortcuts import redirect
from django.db.models import Q
from follow.models import Relation
from post.models import Post
from comment.forms import AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from like.models import Like
from redis import Redis
from django.conf import settings
from django.contrib import messages

# redis connection config
redis_con = Redis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB)


class PostList(ListView):
    model = Post
    template_name = "post/feed.html"

    def get_queryset(self):
        return Post.show_feed(self.request.user)


class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.pcomment.filter(is_reply=False)
        context['comment_form'] = AddCommentForm()
        context['reply_comment_form'] = AddCommentForm()
        context['post_view'] = redis_con.incr(self.object.id)
        if self.request.user.is_authenticated:
            context['is_like'] = self.object.postlike.filter(
                user=self.request.user).exists()
        return context


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('body', 'image')
    template_name = 'post/addpost.html'

    def get_success_url(self, **kwargs):
        messages.success(
            self.request, "Post was created successfully", "success")
        return reverse_lazy('accounts:profile', kwargs={'user': self.request.user})

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.user = self.request.user
        new_post.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post

    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        if not request.user == post.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        messages.error(self.request, "Post was delete successfully", "danger")
        return reverse_lazy('accounts:profile', kwargs={'user': self.request.user})


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post/addpost.html'

    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        if not request.user == post.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)
