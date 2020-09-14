from django.urls import path
from writers.views import (CreateWriterAPI,
                           ActivateWriterAPI,
                           SetupWriterAPI,
                           ManageWriterAPI,
                           DeleteWriterAPI)

urlpatterns = [
    path('create/', CreateWriterAPI.as_view(), name='acc_create'),
    path('activate/<uidb64>/<token>/', ActivateWriterAPI.as_view(), name='acc_activate'),
    path('setup/<int:pk>/', SetupWriterAPI.as_view(), name='acc_setup'),
    path('manage/<str:username>/', ManageWriterAPI.as_view(), name='acc_manage'),
    path('delete/<str:username>/', DeleteWriterAPI.as_view(), name='acc_delete'),
]
