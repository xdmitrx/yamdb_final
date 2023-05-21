from django.urls import include, path
from rest_framework import routers

from reviews.views import CommentViewSet, ReviewViewSet


reviews_v1_router = routers.DefaultRouter()
reviews_v1_router.register(
    r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="review"
)
reviews_v1_router.register(
    r"^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comment",
)

urlpatterns = [
    path("v1/", include(reviews_v1_router.urls)),
]
