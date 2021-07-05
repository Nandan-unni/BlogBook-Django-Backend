from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def index(request):
    return render(request, "api.html")


urlpatterns = [
    path("", index, name="index"),
    path("api/", index, name="api"),
    path("admin/", admin.site.urls),
    path("api/writer/", include("writers.urls")),
    path("api/blog/", include("blogs.urls")),
]
