from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import AddPost, login, register, PostList, UserProfile

app_name = 'accounts'

urlpatterns = [
    path('', PostList.as_view(),name = 'dash'),
    path('login/', login.as_view(),name = 'login'),
    path('register/', register.as_view(),name = 'register'),
    path('logout/', LogoutView.as_view(),name = 'logout'),
    path('addpost/', AddPost.as_view(),name = 'addpost'),
    path('<str:user>/', UserProfile.as_view(),name = 'profile'),




]