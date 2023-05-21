from django.urls import include, path


urlpatterns = [
    path("", include("users.urls")),
    path("", include("titles.urls")),
    path("", include("reviews.urls")),
]
