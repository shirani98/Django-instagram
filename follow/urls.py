from django.urls import path
from .views import FollowerList, FollowingList, UnFollowUser, FollowUser

app_name = 'follow'

urlpatterns = [
    path('follow/<int:id>', FollowUser.as_view(),name = 'follow'),
    path('unfollow/<int:id>', UnFollowUser.as_view(),name = 'unfollow'),
    path('followerlist/<str:user>/', FollowerList.as_view(),name = 'followerlist'),
    path('followinglist/<str:user>/', FollowingList.as_view(),name = 'followinglist'),
]