from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('accounts/create/', views.create_account, name='create_account'),
    path('accounts/message/', views.post_create_account, name='verification_msg'),
    path('accounts/<uidb64>/<token>/', views.activate_account, name='activate_account'),
    path('accounts/<pk>', views.view_blogger, name='view_blogger'),
    path('accounts/view/', views.view_account, name='view_account'),
    path('accounts/edit/', views.edit_account, name='edit_account'),
    path('accounts/editdp/', views.edit_dp, name='edit_dp'),
    path('accounts/delete/', views.delete_account, name='delete_account'),

    path('blogs/<pk>', views.view_blog),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/view/', views.view_blogs, name='view_blogs'),
    path('blogs/edit/<pk>', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<pk>', views.delete_blog, name='delete_blog'),
]