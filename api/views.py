from rest_framework import generics, views, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate, login, logout

from api.serializers import AccountSerializer, BlogSerializer
from app.models import Blog, Writer

def test(request):
    if request.method == 'POST':
        print(request.data)
    return Response(status=status.HTTP_200_OK, data='success')

class LoginAccountAPI(views.APIView):
    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            print(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ManageAccountAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = get_user_model().objects.all()

class CreateBlogAPI(views.APIView):
    def post(self, request, format=None):
        blog = Blog(
            author=get_user_model().objects.get(email='unni@keyblogs.in'),
            title=request.data.get('title'),
            content=request.data.get('content')
        )
        blog.save()
        print(request.data)
        return Response(status=status.HTTP_200_OK)

class ManageBlogAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
