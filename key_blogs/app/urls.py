from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('accounts/create/', views.create_account, name='create_account'),
    path('accounts/activate/<uidb64>/<token>/', views.activate_account, name='activate_account'),
    path('accounts/<username>/<panel>', views.view_account, name='view_account'),
    path('accounts/edit/', views.edit_account, name='edit_account'),
    path('accounts/editdp/', views.edit_dp, name='edit_dp'),
    path('accounts/<username>/follow/', views.follow, name='follow_account'),
    path('accounts/delete/', views.delete_account, name='delete_account'),

    path('blogs/<pk>', views.view_blog),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/view/', views.view_blogs, name='view_blogs'),
    path('blogs/like/<pk>', views.like_blog, name='like_blog'),
    path('blogs/edit/<pk>', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<pk>', views.delete_blog, name='delete_blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
