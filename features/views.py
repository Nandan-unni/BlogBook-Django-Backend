from rest_framework import views, generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate, login, logout

from writers.serializers import WriterSerializer, MiniWriterSerializer
from blogs.serializers import BlogSerializer
from writers.views import message
from blogs.models import Blog


class LoginAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            message(user.name + ' logged in.')
            serializer = WriterSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        message('User not found.')
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class LogoutAPI(views.APIView):
    def get(self, request, **kwargs):
        user = get_user_model().objects.get(pk=kwargs['pk'])
        message(user.name + ' logged out. ')
        logout(request)
        return Response(status=status.HTTP_200_OK)


class FeedAPI(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(is_published=True).order_by('-pub_date')


class SearchAPI(views.APIView):

    def post(self, request, **kwargs):
        writer = request.POST['username']
        bloggers = get_user_model().objects.filter(username=writer)
        serializer = MiniWriterSerializer(data=bloggers)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def get(self, request, **kwargs):
        bloggers = get_user_model().objects.all()
        serializer = MiniWriterSerializer(data=bloggers)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class MessageAPI(views.APIView):
    pass


class NotificationAPI(views.APIView):
    pass