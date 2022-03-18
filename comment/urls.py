from django.urls import path
from .views import AddComment, ReplyView


app_name = 'comment'

urlpatterns = [
    path('addcomment/<slug:slug>/', AddComment.as_view(), name='addcomment'),
    path('addreply/<slug:slug>/<int:cid>',
         ReplyView.as_view(), name='addreply'),
    
]
