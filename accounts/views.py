from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import MyUser
from follow.models import Relation
from django.urls import reverse_lazy
from post.models import Post
from django.http import Http404
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView


class Login(LoginView):

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("post:feed")
        return super().dispatch(request, *args, **kwargs)


class Register(CreateView):
    model = MyUser
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("post:feed")
        return super().dispatch(request, *args, **kwargs)


class UserProfile(ListView):
    template_name = 'accounts/profile.html'

    def dispatch(self, request, *args, **kwargs):
        self.user = MyUser.objects.prefetch_related(
            'fromuser', 'touser', 'userpost').get(username=self.kwargs['user'])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        return self.user.userpost.all()

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['profile'] = self.user
        context['following_count'] = self.user.fromuser.count()
        context['follower_count'] = self.user.touser.count()
        if self.request.user.is_authenticated:
            context['follow'] = self.user.touser.filter(
                from_user__username=self.request.user.username).exists()
        return context


class EditProfile(LoginRequiredMixin, UpdateView):
    model = MyUser
    form_class = UserChangeForm
    template_name = 'accounts/update.html'

    def get_object(self, **kwargs):
        username = self.kwargs.get("user")
        if self.request.user.username != username:
            raise Http404
        return get_object_or_404(MyUser, username__iexact=username)

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:profile', kwargs={'user': self.request.user})


class Explore(LoginRequiredMixin, ListView):
    template_name = 'accounts/explore.html'

    def get_queryset(self, **kwargs):
        return MyUser.objects.filter(is_active=True)


class SearchUser(ListView):
    template_name = 'accounts/explore.html'
    model = MyUser

    def get_queryset(self):
        q = self.request.GET.get('search')
        return MyUser.objects.filter(username__icontains=q)


class ResetPass(PasswordResetView):
    template_name = 'accounts/password/reset.html'
    success_url = reverse_lazy('accounts:resetdone')
    email_template_name = 'accounts/password/password_reset_email.html'


class ResetPassDone(PasswordResetDoneView):
    template_name = 'accounts/password/password_reset_done.html'


class RestPassConfirm(PasswordResetConfirmView):
    template_name = 'accounts/password/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:resetdonecomplete')


class RestPassComplate(PasswordResetCompleteView):
    template_name = 'accounts/password/password_reset_complate.html'
