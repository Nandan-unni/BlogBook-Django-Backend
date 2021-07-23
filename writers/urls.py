from django.urls import path
from writers.views import (
    UsernameAndEmails,
    SetupWriterAPI,
    ManageWriterAPI,
    DeleteWriterAPI,
    SearchWriterAPI,
    FollowWriterAPI,
)

urlpatterns = [
    path("usernamesandemails/", UsernameAndEmails.as_view(), name="livecheck"),
    path("setup/<int:pk>/", SetupWriterAPI.as_view(), name="acc_setup"),
    path("manage/<int:pk>/", ManageWriterAPI.as_view(), name="acc_manage"),
    path("delete/<int:pk>/", DeleteWriterAPI.as_view(), name="acc_delete"),
    path("search/", SearchWriterAPI.as_view(), name="acc_search"),
    path(
        "follow/<int:user_pk>/<int:writer_pk>/",
        FollowWriterAPI.as_view(),
        name="acc_follow",
    ),
]
