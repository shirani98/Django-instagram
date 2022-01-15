from xml.parsers.expat import model
from django.contrib.auth.views import LoginView
from django.http.response import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from .models import MyUser
from follow.models import Relation
from django.urls import reverse_lazy
from post.models import Post
from django.http import HttpResponseRedirect, Http404
from .forms import ProfileEditForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

class Login(LoginView):
    template_name = 'accounts/login.html'
class Register(CreateView):
    model = MyUser
    form_class = UserRegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'
class UserProfile(ListView):
    def get_queryset(self, **kwargs):
        return Post.objects.filter(user__username = self.kwargs['user'])
    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['profile'] = MyUser.objects.get(username = self.kwargs['user'])
        context['following_count'] = Relation.objects.filter(from_user__username = self.kwargs['user']).count()
        context['follower_count'] = Relation.objects.filter(to_user__username = self.kwargs['user']).count()
        if self.request.user.is_authenticated:
            context['follow'] = Relation.objects.filter(from_user = self.request.user, to_user__username = self.kwargs['user']).exists()
        return context
    template_name = 'accounts/profile.html'
class EditProfile(LoginRequiredMixin,UpdateView):
    model = MyUser
    form_class = ProfileEditForm
    template_name = 'accounts/update.html'
    
    def get_object(self, **kwargs):
        username = self.kwargs.get("user")
        if self.request.user.username != username:
            raise Http404
        return get_object_or_404(MyUser,username__iexact=username)    
    def get_context_data(self, **kwargs):
        context = super(EditProfile, self).get_context_data(**kwargs)
        context['profile'] = MyUser.objects.get(username = self.kwargs['user'])
        return context
    def get_success_url(self, **kwargs):         
        return reverse_lazy('accounts:profile', kwargs = {'user': self.request.user})

class Explore(LoginRequiredMixin,ListView):
    def get_queryset(self, **kwargs):
        return MyUser.objects.filter(is_active = True)
    template_name = 'accounts/explore.html'
    
class SearchUser(ListView):
    template_name = 'accounts/explore.html'
    model = MyUser
    def get_queryset(self):
        q = self.request.GET.get('search')
        return MyUser.objects.filter(username__icontains=q)
    
        
        
            