from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import login, register, PostList

app_name = 'accounts'

urlpatterns = [
    path('dash/', PostList.as_view(),name = 'dash'),
    path('login/', login.as_view(),name = 'login'),
    path('register/', register.as_view(),name = 'register'),
    path('logout/', LogoutView.as_view(),name = 'logout'),
    


]