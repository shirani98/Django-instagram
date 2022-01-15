from django.urls import path

from .views import FollowerList, FollowingList, UnfollowUser, followUser

app_name = 'follow'
urlpatterns = [
    path('follow/<int:id>', followUser,name = 'follow'),
    path('unfollow/<int:id>', UnfollowUser,name = 'unfollow'),
    path('followerlist/<str:user>/', FollowerList.as_view(),name = 'followerlist'),
    path('followinglist/<str:user>/', FollowingList.as_view(),name = 'followinglist'),
]