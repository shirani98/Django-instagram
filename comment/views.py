from django.views.generic.edit import CreateView
from post.models import Post
from .models import Comment
from .forms import AddCommentForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin 
# Create your views here.

class ReplyView(LoginRequiredMixin , CreateView):
    model = Comment
    form_class = AddCommentForm
    
    def post(self, *args, **kwargs):
        reply = self.request.POST.get('body')
        postslug = self.kwargs.get('slug')
        commentid = self.kwargs.get('cid')
        post = Post.objects.get(slug=postslug)
        comment = Comment.objects.get(id = commentid)
        Comment.objects.create(body=reply,user= self.request.user,post = post,is_reply=True,reply = comment )
        return redirect('post:detail',post.slug)
    
