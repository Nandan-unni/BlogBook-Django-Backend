from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('features.urls')),
    path('api/writer/', include('writers.urls')),
    path('api/blog/', include('blogs.urls')),
]
