from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.models import Blog

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = get_user_model()
        fields = ['name', 'email', 'username', 'password']

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'is_published']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['pk', 'author', 'author_pname', 'title', 'content', 'likes', 'no_of_likes', 'is_published']

class AccountSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ['pk', 'name', 'username', 'email',
                  'bio', 'dp',
                  'followers', 'no_of_followers',
                  'following', 'no_of_following',
                  'blogs', 'no_of_blogs']
