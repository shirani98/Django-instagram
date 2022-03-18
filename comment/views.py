from django.views.generic.edit import CreateView
from post.models import Post
from comment.models import Comment
from comment.forms import AddCommentForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = AddCommentForm

    def post(self, *args, **kwargs):
        return Comment.create_comment(
            self.request.POST.get('body'),
            self.kwargs.get('slug'),
            self.request.user)


class ReplyView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = AddCommentForm

    def post(self, *args, **kwargs):
        return Comment.create_reply(
            self.request.POST.get('body'),
            self.kwargs.get('slug'),
            self.kwargs.get('cid'),
            self.request.user)
