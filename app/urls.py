from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import *

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('accounts/create/',
         create_account,
         name='create_account'),

    path('accounts/username/<pk>',
         CreatePenNameView.as_view(),
         name='create_username'),

    path('accounts/activate/<uidb64>/<token>/',
         activate_account,
         name='activate_account'),

    path('accounts/<slug>/<panel>',
         login_required(AccountView.as_view()),
         name='view_account'),

    path('accounts/<slug>/edit/',
         login_required(EditAccountView.as_view()),
         name='edit_account'),

    path('accounts/<slug>/editdp/',
         login_required(EditDPView.as_view()),
         name='edit_dp'),

    path('accounts/<username>/follow/',
         follow,
         name='follow_account'),

    path('accounts/delete/',
         delete_account,
         name='delete_account'),


    path('blogs/<pk>',
         login_required(BlogView.as_view()),
         name='view_blog'),

    path('blogs/create/', 
         login_required(CreateBlogView.as_view()),
         name='create_blog'),

    path('blogs/view/',
         login_required(BlogsView.as_view()),
         name='view_blogs'),

    path('blogs/like/<pk>',
         like_blog,
         name='like_blog'),

    path('blogs/edit/<pk>',
         login_required(EditBlogView.as_view()),
         name='edit_blog'),

    path('blogs/delete/<pk>',
         login_required(DeleteBlogView.as_view()),
         name='delete_blog'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
