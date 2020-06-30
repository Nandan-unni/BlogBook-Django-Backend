from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('feeds/', views.feeds, name='feeds'),
    path('create/', views.create_blog, name='create_blog')
]