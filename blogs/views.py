from blogs.utils import get_summary
from rest_framework import generics, views, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from writers.views import message
from blogs.models import Blog
from blogs.serializers import BlogSerializer


class CreateBlogAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        blog = Blog(
            author=get_user_model().objects.get(pk=request.data.get("author")),
            title=request.data.get("title"),
            content=request.data.get("content"),
            summary=get_summary(request.data.get("content")),
            is_published=request.data.get("is_published"),
        )
        blog.save()
        return Response(status=status.HTTP_200_OK)


class ManageBlogAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def patch(self, request, *args, **kwargs):
        if request.data["content"]:
            request.data["summary"] = get_summary(request.data.get("content"))
        return super().patch(request, *args, **kwargs)


class LikeBlogAPI(views.APIView):
    def get(self, request, **kwargs):
        blog = Blog.objects.get(pk=kwargs["blog_pk"])
        user = get_user_model().objects.get(pk=kwargs["writer_pk"])
        if user in blog.likes.all():
            blog.likes.remove(user)
            message(
                f"{user.name} ({user.pk}) unliked the blog '{blog.title}' ({blog.pk})"
            )
        else:
            blog.likes.add(user)
            message(
                f"{user.name} ({user.pk}) liked the blog '{blog.title}' ({blog.pk})"
            )
        serializer = BlogSerializer(blog)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SaveBlogAPI(views.APIView):
    def get(self, request, **kwargs):
        blog = Blog.objects.get(pk=kwargs["blog_pk"])
        user = get_user_model().objects.get(pk=kwargs["writer_pk"])
        if user in blog.saves.all():
            blog.saves.remove(user)
            message(
                f"{user.name} ({user.pk}) unsaved the blog '{blog.title}' ({blog.pk})"
            )
        else:
            blog.saves.add(user)
            message(
                f"{user.name} ({user.pk}) saved the blog '{blog.title}' ({blog.pk})"
            )
        serializer = BlogSerializer(blog)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class FeedAPI(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(is_published=True).order_by("-pub_date")
