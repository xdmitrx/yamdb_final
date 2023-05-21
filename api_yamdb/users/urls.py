from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    get_jwt_token,
    get_or_update_account_details,
    send_confirmation_code,
)


users_v1_router = DefaultRouter()
users_v1_router.register(r"users", UserViewSet, basename="user")

auth_patterns = [
    path("signup/", send_confirmation_code),
    path("token/", get_jwt_token),
]

urlpatterns = [
    path("v1/auth/", include(auth_patterns)),
    path("v1/users/me/", get_or_update_account_details),
    path("v1/", include(users_v1_router.urls)),
]
