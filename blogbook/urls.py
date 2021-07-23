from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def index(request):
    return render(request, "api.html")


urlpatterns = [
    path("", index, name="index"),
    path("api/", index, name="api"),
    path("admin/", admin.site.urls),
    # path("api/token/auth", TokenObtainPairView.as_view(), name="auth_token"),
    # path("api/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/auth/", include("auth.urls")),
    path("api/writer/", include("writers.urls")),
    path("api/blog/", include("blogs.urls")),
]
