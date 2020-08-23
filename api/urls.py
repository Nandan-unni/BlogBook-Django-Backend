from django.urls import path
from .views import *

urlpatterns = [
    path('account/login/', LoginAccountAPI.as_view(), name='login_account'),
    path('account/logout/', LogoutAccountAPI.as_view(), name='logout_account'),
    path('account/create/', CreateAccountAPI.as_view(), name='create_account'),
    path('account/manage/<int:pk>', ManageAccountAPI.as_view(), name='manage_account'),
    path('blog/create/', CreateBlogAPI.as_view(), name='create_blog'),
    path('blog/manage/<int:pk>', ManageBlogAPI.as_view(), name='manage_blog')
]
