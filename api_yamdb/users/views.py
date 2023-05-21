from django.contrib.auth import get_user_model
from rest_framework import filters, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .permissions import IsAdminRoleOrSuperUser
from .serializers import (
    AccountDetailsSerializer,
    ConfirmationCodeSerializer,
    RegistratingUserSerializer,
    UserSerializer,
)
from .services import get_access_token_for_user


User = get_user_model()


@api_view(["POST"])
@permission_classes([AllowAny])
def send_confirmation_code(request):
    data = request.data
    serializer = RegistratingUserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Response(request.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def get_jwt_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data["user"]
    token = get_access_token_for_user(user)
    return Response({"token": f"{token}"})


@api_view(["GET", "PATCH"])
@permission_classes([IsAuthenticated])
def get_or_update_account_details(request):
    serializer = AccountDetailsSerializer(
        request.user, data=request.data, partial=True
    )
    serializer.is_valid(raise_exception=True)

    if request.method == "PATCH":
        serializer.save()
    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = "username"
    serializer_class = UserSerializer
    permission_classes = (IsAdminRoleOrSuperUser, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("username",)
