from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from post.models import Post
from django.utils.text import slugify

from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:dash')

class register(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(user = self.request.user)
    template_name = 'accounts/dash.html'
class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('body',)
    template_name = 'post/addpost.html'
    success_url = reverse_lazy('accounts:dash')
    def form_valid(self,form):
        new_post = form.save(commit=False)
        new_post.user = self.request.user
        new_post.slug = slugify(form.cleaned_data['body'][:10])
        new_post.save()
        return super().form_valid(form)
class UserProfile(ListView):
    def get_queryset(self, **kwargs):
        return Post.objects.filter(user__username = self.kwargs['user'])
    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['profile'] = User.objects.get(username = self.kwargs['user'])
        return context
    template_name = 'accounts/profile.html'
    



