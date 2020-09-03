from django.urls import path
from .views import *

urlpatterns = [
    path('account/login/', LoginAccountAPI.as_view(), name='login_account_api'),
    path('account/logout/<int:pk>', LogoutAccountAPI.as_view(), name='logout_account_api'),
    path('account/create/', CreateAccountAPI.as_view(), name='create_account_api'),
    path('account/activate/<uidb64>/<token>/', ActivateAccountAPI.as_view(), name='activate_account_api'),
    path('account/username/<pk>', CreatePnameAPI.as_view(), name='create_username_api'),
    path('account/manage/<username>', ManageAccountAPI.as_view(), name='manage_account_api'),
    path('account/delete/<username>', DeleteAccountAPI.as_view(), name='delete_account_api'),
    path('blog/create/', CreateBlogAPI.as_view(), name='create_blog_api'),
    path('blog/manage/<int:pk>', ManageBlogAPI.as_view(), name='manage_blog_api'),
    path('blog/like/<int:blog_pk>/<int:user_pk>', LikeBlogAPI.as_view(), name='like_blog_api'),
    path('feed/', FeedAPI.as_view(), name='feeds_api'),
]
