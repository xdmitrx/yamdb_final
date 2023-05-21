from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken


def generate_confirmation_code(user):
    return default_token_generator.make_token(user)


def is_confirmation_code_valid(user, confirmation_code):
    return default_token_generator.check_token(user, confirmation_code)


def get_access_token_for_user(user):
    return str(RefreshToken.for_user(user).access_token)


def send_mail_to_user(email, topic, text, username="Дорогой друг"):
    send_mail(
        f"{topic}",
        f"Добрый день, {username}!\n\n{text}",
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
