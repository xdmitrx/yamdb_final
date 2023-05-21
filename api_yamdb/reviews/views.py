from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.models import Comment, Review
from reviews.permissions import IsAuthorModeratorAdminOrReadOnly
from reviews.serializers import CommentSerializer, ReviewSerializer
from titles.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def get_title(self):

        return get_object_or_404(Title, pk=self.kwargs.get("title_id"))

    def get_queryset(self):

        return get_object_or_404(
            Title, pk=self.kwargs.get("title_id")
        ).reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def get_review(self):

        return get_object_or_404(
            Review,
            pk=self.kwargs.get("review_id"),
            title__id=self.kwargs.get("title_id"),
        )

    def get_queryset(self):

        return get_object_or_404(
            Review,
            pk=self.kwargs.get("review_id"),
            title__id=self.kwargs.get("title_id"),
        ).comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())
