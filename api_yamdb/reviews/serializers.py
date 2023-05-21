from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Comment, Review
from titles.models import Title


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Comment
        fields = ("id", "author", "pub_date", "text")
        read_only_fields = ("id", "author", "pub_date")


class ReviewSerializer(serializers.ModelSerializer):
    title = SlugRelatedField(
        slug_field="name",
        read_only=True,
    )
    author = SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field="username",
        read_only=True,
    )
    score = serializers.IntegerField(
        validators=[
            MinValueValidator(1, "Оценка должна быть не меньше 1."),
            MaxValueValidator(10, "Оценка должна быть не больше 10."),
        ],
    )

    class Meta:
        model = Review
        fields = "__all__"

    def validate(self, data):
        if self.context["request"].method == "POST":
            title_id = self.context.get("view").kwargs.get("title_id")
            title = get_object_or_404(Title, id=title_id)
            request = self.context["request"]
            author = request.user
            if Review.objects.filter(title=title, author=author).exists():
                raise serializers.ValidationError(
                    "Вы уже оставили свой отзыв" "к этому произведению!"
                )
        return data
