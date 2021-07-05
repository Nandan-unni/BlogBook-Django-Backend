from django.urls import path
from writers.views import (
    LoginWriterAPI,
    LogoutWriterAPI,
    CreateWriterAPI,
    ActivateWriterAPI,
    SetupWriterAPI,
    ManageWriterAPI,
    DeleteWriterAPI,
    SearchWriterAPI,
    FollowWriterAPI,
)

urlpatterns = [
    path("login/", LoginWriterAPI.as_view(), name="signin"),
    path("logout/<int:pk>/", LogoutWriterAPI.as_view(), name="signout"),
    path("create/", CreateWriterAPI.as_view(), name="signup"),
    path(
        "activate/<uidb64>/<token>/", ActivateWriterAPI.as_view(), name="acc_activate"
    ),
    path("setup/<int:pk>/", SetupWriterAPI.as_view(), name="acc_setup"),
    path("manage/<str:username>/", ManageWriterAPI.as_view(), name="acc_manage"),
    path("delete/<str:username>/", DeleteWriterAPI.as_view(), name="acc_delete"),
    path("search/", SearchWriterAPI.as_view(), name="acc_search"),
    path(
        "follow/<int:user_pk>/<int:writer_pk>/",
        FollowWriterAPI.as_view(),
        name="acc_follow",
    ),
]
