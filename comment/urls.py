from django.urls import path
from comment.views import CommentCreate

app_name = 'comment'
urlpatterns = [
    path('addcomment/<slug:slug>',CommentCreate.as_view(),name = 'addcomment'),
]