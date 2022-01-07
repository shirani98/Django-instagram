from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import EditProfile, login, register, UserProfile
from post.views import AddPost, DeletePost, EditPost
app_name = 'accounts'

urlpatterns = [
    path('login/', login.as_view(),name = 'login'),
    path('register/', register.as_view(),name = 'register'),
    path('logout/', LogoutView.as_view(),name = 'logout'),
    path('addpost/', AddPost.as_view(),name = 'addpost'),
    path('<str:user>/', UserProfile.as_view(),name = 'profile'),
    path('<str:user>/edit', EditProfile.as_view(),name = 'editprofile'),
    path('del/<slug:slug>', DeletePost.as_view(),name = 'del'),
    path('edit/<slug:slug>', EditPost.as_view(),name = 'edit'),





]