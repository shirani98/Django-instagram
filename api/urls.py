from django.urls import path
from .views import CreateListComment, DisLikePost, FollowUser, LikePost, PostCreate, PostListFeed, PostDetail, PostDelete, PostUpdate, UnFollowUser, UpdateComment, UserDelete, UserList, UserProfile, UserUpdate
from rest_framework_simplejwt import views as jwt_views

app_name = "api"

urlpatterns = [

    # JWT Token
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # Post App Api
    path('post/<int:pk>/', PostDetail.as_view(), name='postdetail'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='postdelete'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='postupdate'),
    path('post/create/', PostCreate.as_view(), name='postcreate'),
    path('post/', PostListFeed.as_view(), name='feed'),

    # Accounts App Api
    path('accounts/<str:username>/', UserProfile.as_view(), name='myuserdetail'),
    path('accounts/<str:username>/delete/',
         UserDelete.as_view(), name='myuserdelete'),
    path('accounts/<str:username>/update/',
         UserUpdate.as_view(), name='myuserupdate'),
    path('accounts/', UserList.as_view(), name='myuserlist'),

    # Like App Api
    path('like/<int:post>/', LikePost.as_view(), name='like'),
    path('dislike/<int:post>/', DisLikePost.as_view(), name='dislike'),

    # Follow App Api
    path('follow/<str:to_user>/', FollowUser.as_view(), name='follow'),
    path('unfollow/<str:to_user>/', UnFollowUser.as_view(), name='unfollow'),

    # Comment App Api
    path('comment/<int:post>/', CreateListComment.as_view(), name='createcomment'),
    path('comment/update/<int:pk>/', UpdateComment.as_view(), name='updatecomment'),



]
