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
        fields = ['title', 'content']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['pk', 'author', 'title', 'content', 'pub_time', 'likes', 'no_of_likes']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'name', 'email',
                  'bio', 'dp',
                  'followers', 'no_of_followers',
                  'following', 'no_of_following']
