from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import User
from .services import (
    generate_confirmation_code,
    is_confirmation_code_valid,
    send_mail_to_user,
)


class RegistratingUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate_username(self, value):
        if value == "me":
            raise serializers.ValidationError(
                "Использовать имя 'me' в качестве username запрещено."
            )
        return value

    def validate(self, data):
        email, username = data["email"], data["username"]
        username_query = User.objects.filter(username=username)
        email_query = User.objects.filter(email=email)

        if not username_query.exists() and not email_query.exists():
            user = User.objects.create(email=email, username=username)
            user.save()
            topic = "Код подтверждения"
            confirmation_code = generate_confirmation_code(user)
            text = f"Ваш код подтверждения: {confirmation_code}"
            send_mail_to_user(email, topic, text, username)

        elif username_query.exists() and not email_query.exists():
            raise serializers.ValidationError("Такой username уже существует.")

        else:
            existing_user = email_query[0]
            existing_username = existing_user.username
            confirmation_code = generate_confirmation_code(existing_user)
            topic = "Код подтверждения (повторно)"
            text = (
                f"Ваш код подтверждения: {confirmation_code}\n"
                f"Ваш юзернейм при регистрации: {existing_username}"
            )
            send_mail_to_user(email, topic, text, existing_username)

            raise serializers.ValidationError(
                "Письмо с кодом подтверждения отправлено повторно."
            )
        return data


class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        confirmation_code, username = (
            data["confirmation_code"],
            data["username"],
        )
        user = get_object_or_404(User, username=username)
        if not is_confirmation_code_valid(user, confirmation_code):
            raise serializers.ValidationError("Неверный код подтверждения")
        return {**data, **{"user": user}}


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
        model = User
        read_only_fields = ("role",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
        model = User
