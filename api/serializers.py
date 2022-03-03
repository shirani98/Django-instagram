from django.conf import settings
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from redis import Redis
from rest_framework import serializers
from follow.models import Relation
from like.models import Like
from post.models import Post
from accounts.models import MyUser
from comment.models import Comment


redis_con = Redis(settings.REDIS_HOST, settings.REDIS_PORT,
                  settings.REDIS_DB, decode_responses=True)

# Post Serializers


class UserInfoPost(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'avatar')


class CommentInfo(serializers.ModelSerializer):
    user = UserInfoPost()

    class Meta:
        model = Comment
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    user = UserInfoPost()
    like = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'slug')

    def get_like(self, obj):
        return obj.postlike.all().count()

    def get_comment(self, obj):
        return obj.pcomment.all().count()


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserInfoPost()
    like = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    view = serializers.SerializerMethodField()
    pcomment = CommentInfo(many=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'slug')

    def get_like(self, obj):
        return obj.postlike.all().count()

    def get_comment_count(self, obj):
        return obj.pcomment.all().count()

    def get_view(self, obj):
        return redis_con.incr(obj.id)


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'slug')


# Accounts Serializers
class UserDetailSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    follower = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    userpost = PostListSerializer(many=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'firstname', 'lastname', 'bio',
                  'avatar', 'post_count', 'userpost', 'follower', 'following')

    def get_post_count(self, obj):
        return obj.userpost.all().count()

    def get_follower(self, obj):
        return obj.touser.all().count()

    def get_following(self, obj):
        return obj.fromuser.all().count()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'avatar')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'firstname', 'lastname',
                  'phone', 'avatar', 'bio')

# Like Serializer


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post', 'user')
        read_only_fields = ('post', 'user')

# Follow Serializer


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ('from_user', 'to_user', 'created')
        read_only_fields = ('from_user', 'to_user')

# Comment Serializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'user')

    def validate(self, attrs):
        if len(attrs['body']) > 30:
            raise ValidationError("Error !")
        return attrs
