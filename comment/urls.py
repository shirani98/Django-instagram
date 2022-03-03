from django.urls import path
from .views import ReplyView


app_name = 'comment'

urlpatterns = [
    
    path('addreply/<slug:slug>/<int:cid>',
         ReplyView.as_view(), name='addreply'),
    
]
