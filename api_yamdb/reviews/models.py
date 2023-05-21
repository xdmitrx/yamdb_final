from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from titles.models import Title

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Название произведения",
    )
    text = models.TextField(max_length=200, verbose_name="Текст обзора")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Автор",
    )
    score = models.PositiveIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(10)),
        error_messages={"validators": "Оценка от 1 до 10!"},
        verbose_name="Оценка",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "title",
                    "author",
                ),
                name="unique review",
            )
        ]
        ordering = ("pub_date",)

    def __str__(self):
        return f"<{self.text[:64]}>"


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Обзор",
    )
    text = models.TextField(
        max_length=200,
        verbose_name="Текст комментария",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("pub_date",)

    def __str__(self):
        return f"<{self.text[:64]}>"
