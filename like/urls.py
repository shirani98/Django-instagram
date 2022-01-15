from django.urls import path
from .views import like_post, unlike,LikeList
app_name = 'like'
urlpatterns = [
    path('<int:postid>/',like_post, name = 'like_url'),
    path('unlike/<int:postid>/',unlike, name = 'unlike_url'),
    path('listlike/<slug:slug>',LikeList.as_view(), name = 'listlike'),

]