from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=200)
    slug = models.SlugField(verbose_name="Слаг категории", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-id"]

    def __str__(self):
        return f"<{self.slug}>"


class Genre(models.Model):
    name = models.CharField(verbose_name="Название жанра", max_length=200)
    slug = models.SlugField(verbose_name="Слаг жанра", unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ["-id"]

    def __str__(self):
        return f"<{self.slug}>"


class Title(models.Model):
    name = models.CharField(
        verbose_name="Название произведения", max_length=200
    )
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(2100), MinValueValidator(1900)],
        db_index=True,
        verbose_name="Год",
    )
    description = models.TextField(null=True, verbose_name="Описание")
    category = models.ForeignKey(
        Category,
        related_name="titles",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
    )
    genre = models.ManyToManyField(
        Genre, through="GenreTitle", verbose_name="Жанр"
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"
        ordering = ["-id"]

    def __str__(self):
        return f"<{self.name}>"


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, verbose_name="Произведение"
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, verbose_name="Жанр"
    )

    def __str__(self):
        return f"<{self.title.name} - {self.genre.slug}>"
