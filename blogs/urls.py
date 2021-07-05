from django.urls import path
from blogs.views import CreateBlogAPI, ManageBlogAPI, LikeBlogAPI, SaveBlogAPI, FeedAPI

urlpatterns = [
    path("feed/", FeedAPI.as_view(), name="feed"),
    path("create/", CreateBlogAPI.as_view(), name="blog_create"),
    path("manage/<int:pk>/", ManageBlogAPI.as_view(), name="blog_manage"),
    path(
        "like/<int:writer_pk>/<int:blog_pk>/", LikeBlogAPI.as_view(), name="blog_like"
    ),
    path(
        "save/<int:writer_pk>/<int:blog_pk>/", SaveBlogAPI.as_view(), name="blog_save"
    ),
]
