from rest_framework import generics, views, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate, login, logout
from colorama import Fore, Style

from api.serializers import CreateUserSerializer, AccountSerializer, BlogSerializer
from app.models import Blog, Writer

def message(msg):
    print(Fore.MAGENTA, Style.BRIGHT, '\b\b[#]', Fore.RED, msg, Style.RESET_ALL)

class LoginAccountAPI(views.APIView):
    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            message(user.name + ' logged in.')
            return Response(status=status.HTTP_200_OK)
        message('User not found.')
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

class LogoutAccountAPI(views.APIView):
    def get(self, request, format=None):
        message(request.user.name + ' logged out. ')
        logout(request)
        return Response(status=status.HTTP_200_OK)

class CreateAccountAPI(views.APIView):
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            message(user.name + ' created an account.')
            return Response(status=status.HTTP_201_CREATED)
        message(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class ManageAccountAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = get_user_model().objects.all()
    lookup_field = "username"
    def delete(self, request, *args, **kwargs):
        email = request.user.email
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            return super().delete(self, request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class CreateBlogAPI(views.APIView):
    def post(self, request, format=None):
        blog = Blog(
            author=get_user_model().objects.get(email='unni@key.in'),
            title=request.data.get('title'),
            content=request.data.get('content'),
            is_published=request.data.get('is_published')
        )
        blog.save()
        print(request.data)
        return Response(status=status.HTTP_200_OK)

class ManageBlogAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class FeedAPI(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(is_published=True).order_by('-pub_time')
