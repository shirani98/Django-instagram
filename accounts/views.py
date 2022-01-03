from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from post.models import Post
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
    

