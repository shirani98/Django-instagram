from django.urls import path
from .views import PostDetail, PostList

app_name = "post"

urlpatterns = [
    path('',PostList.as_view(),name = 'index'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',PostDetail.as_view(),name = 'detail'),

]