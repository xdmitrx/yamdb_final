from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"

    USER_ROLES = (
        (ADMIN, "Администратор"),
        (MODERATOR, "Модератор"),
        (USER, "Аутентифицированный пользователь"),
    )

    email = models.EmailField(
        verbose_name="E-mail", unique=True, null=False, blank=False
    )
    bio = models.TextField(
        verbose_name="Биография", max_length=512, blank=True
    )
    role = models.CharField(
        verbose_name="Пользовательская роль",
        max_length=16,
        choices=USER_ROLES,
        default="user",
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self):
        return f"<{self.username}>"
