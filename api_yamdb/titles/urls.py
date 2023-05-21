from django.urls import include, path
from rest_framework import routers

from titles.views import CategoryViewSet, GenreViewSet, TitleViewSet


titles_v1_router = routers.DefaultRouter()
titles_v1_router.register(r"titles", TitleViewSet, basename="title")
titles_v1_router.register(r"categories", CategoryViewSet, basename="category")
titles_v1_router.register(r"genres", GenreViewSet, basename="genre")

urlpatterns = [
    path("v1/", include(titles_v1_router.urls)),
]
