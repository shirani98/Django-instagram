from django.urls import path
from .views import LikePost, UnLikePost,LikeList

app_name = 'like'

urlpatterns = [
    path('<int:postid>/',LikePost.as_view(), name = 'like_url'),
    path('unlike/<int:postid>/',UnLikePost.as_view(), name = 'unlike_url'),
    path('listlike/<slug:slug>',LikeList.as_view(), name = 'listlike'),

]