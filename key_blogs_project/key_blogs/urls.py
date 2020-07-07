from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('feeds/', views.feeds, name='feeds'),
    path('profile/', views.profile_view, name='view_profile'),
    path('dpupload/', views.upload_dp, name='upload_dp'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/like', views.like_blog, name='like')
]