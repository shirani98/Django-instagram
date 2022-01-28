from django.urls import path
from .views import PostDetail, PostList, AddPost, DeletePost, EditPost

app_name = "post"

urlpatterns = [
    path('addpost/', AddPost.as_view(),name = 'addpost'),
    path('<slug:slug>/',PostDetail.as_view(),name = 'detail'),
    path('del/<slug:slug>/', DeletePost.as_view(),name = 'del'),
    path('edit/<slug:slug>/', EditPost.as_view(),name = 'edit'),
    path('',PostList.as_view(),name = 'feed'),

]