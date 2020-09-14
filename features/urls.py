from django.urls import path
from features.views import (LoginAPI,
                            LogoutAPI,
                            FeedAPI,
                            SearchAPI,
                            MessageAPI)

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('feed/', FeedAPI.as_view(), name='feed'),
    path('search/', SearchAPI.as_view(), name='search'),
    path('message/', MessageAPI.as_view(), name='message'),
]
