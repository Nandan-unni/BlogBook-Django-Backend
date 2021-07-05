from rest_framework import serializers
from django.contrib.auth import get_user_model

from blogs.serializers import BlogSerializer


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ["name", "email", "username", "password"]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class MiniWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["name", "username", "dp"]


class WriterSerializer(serializers.ModelSerializer):
    pub_blogs = BlogSerializer(many=True)
    arch_blogs = BlogSerializer(many=True)
    saved_blogs = BlogSerializer(many=True)
    followers = MiniWriterSerializer(many=True)
    following = MiniWriterSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = [
            "pk",
            "name",
            "username",
            "email",
            "bio",
            "dp",
            "is_superuser",
            "followers",
            "no_of_followers",
            "following",
            "no_of_following",
            "pub_blogs",
            "no_of_blogs",
            "arch_blogs",
            "saved_blogs",
        ]
