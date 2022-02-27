from comment.models import Comment
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from follow.models import Relation
from like.models import Like
from post.models import Post
from accounts.models import MyUser
from .serializers import CommentSerializer, FollowSerializer, LikeSerializer, PostDetailSerializer, PostListSerializer, PostCreateUpdateSerializer, UserDetailSerializer, UserListSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly
from django.db.models import Q


#Post App API
class PostListFeed(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        super().get_queryset()
        if self.request.user.is_authenticated:
            followed_people = Relation.objects.filter(from_user=self.request.user).values('to_user')
            queryset = Post.objects.filter(Q(user__in = followed_people) | Q(user = self.request.user))
            return queryset
        else:
            return self.queryset.all()


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostDelete(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = self.request.user)


class PostUpdate(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = self.request.user)


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user )


#Accounts App API
class UserProfile(RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

class UserList(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserListSerializer


class UserDelete(RetrieveDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(username = self.request.user)


class UserUpdate(RetrieveUpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(username = self.request.user)

#Like App API
class LikePost(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user, post_id = self.kwargs['post'])

class DisLikePost(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = Like.objects.filter(user = self.request.user.id, post = self.kwargs['post'])
        return obj

#Follow App API
class FollowUser(CreateAPIView):
    queryset = Relation.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user_for_follow = get_object_or_404(MyUser , username = self.kwargs['to_user'])
        serializer.save(from_user = self.request.user , to_user = user_for_follow)

class UnFollowUser(DestroyAPIView):
    queryset = Relation.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = get_object_or_404(MyUser , username = self.kwargs['to_user'])
        obj = Relation.objects.get(from_user = self.request.user , to_user = user)
        return obj

#Comment App API
class CreateListComment(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        post= get_object_or_404(Post, id =self.kwargs['post'])
        return Comment.objects.filter(post = post)


    def perform_create(self, serializer):
        post = get_object_or_404 (Post, id = self.kwargs['post'])
        serializer.save(post = post, user = self.request.user)

class UpdateComment(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)