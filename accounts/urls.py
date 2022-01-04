from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import AddPost, EditPost, login, register, PostList, UserProfile,DeletePost

app_name = 'accounts'

urlpatterns = [
    path('', PostList.as_view(),name = 'dash'),
    path('login/', login.as_view(),name = 'login'),
    path('register/', register.as_view(),name = 'register'),
    path('logout/', LogoutView.as_view(),name = 'logout'),
    path('addpost/', AddPost.as_view(),name = 'addpost'),
    path('<str:user>/', UserProfile.as_view(),name = 'profile'),
    path('del/<slug:slug>', DeletePost.as_view(),name = 'del'),
    path('edit/<slug:slug>', EditPost.as_view(),name = 'edit'),





]