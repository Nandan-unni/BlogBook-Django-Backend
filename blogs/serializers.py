from rest_framework import serializers
from django.contrib.auth import get_user_model

from blogs.models import Blog


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["author", "title", "content", "is_published"]


class MiniWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["name", "username", "dp"]


class BlogSerializer(serializers.ModelSerializer):
    likes = MiniWriterSerializer(many=True)
    saves = MiniWriterSerializer(many=True)
    author = MiniWriterSerializer()

    class Meta:
        model = Blog
        fields = [
            "pk",
            "author",
            "title",
            "content",
            "likes",
            "no_of_likes",
            "saves",
            "is_published",
        ]
