from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feeds/', views.feeds, name='feeds'),
    path('accounts/create', views.create_account, name='create_account'),
    path('accounts/view', views.view_account, name='view_account'),
    path('accounts/edit', views.edit_account, name='edit_account'),
    path('accounts/delete', views.delete_account, name='delete_account'),
    path('blogs/create', views.create_blog, name='create_blog'),
    path('blogs/edit', views.edit_blog, name='edit_blog'),
    path('blogs/delete', views.delete_blog, name='delete_blog'),
]