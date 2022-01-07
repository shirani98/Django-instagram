from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from post.models import Post
from django.http import HttpResponseRedirect, Http404
from .forms import ProfileEditForm, UserEditForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.shortcuts import get_object_or_404
class login(LoginView):
    template_name = 'accounts/login.html'
class register(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'
class UserProfile(ListView):
    def get_queryset(self, **kwargs):
        return Post.objects.filter(user__username = self.kwargs['user'])
    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['profile'] = User.objects.get(username = self.kwargs['user'])
        return context
    template_name = 'accounts/profile.html'
class EditProfile(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/update.html'
    
    def get_object(self, **kwargs):
        username = self.kwargs.get("user")
        if self.request.user.username != username:
            raise Http404
        return get_object_or_404(Profile, user__username__iexact=username)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formuser'] = UserEditForm(instance=self.request.user)
        return context
    
    def post(self, *args, **kwargs):
        form = ProfileEditForm(self.request.POST, instance = self.request.user.profile)
        form2 = UserEditForm(self.request.POST, instance = self.request.user)
        
        if form.is_valid() and form2.is_valid():
            userdata = form.save(commit=False)
            userdata.user = self.request.user
            userdata.save()
            employeedata = form2.save(commit=False)
            employeedata.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
              self.get_context_data(form=form, form2=form2))
    def get_success_url(self, **kwargs):         
        return reverse_lazy('accounts:profile', kwargs = {'user': self.request.user})
