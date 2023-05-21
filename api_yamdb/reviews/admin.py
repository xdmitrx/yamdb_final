from django.contrib import admin

from .models import Comment, Review


class CommentAdmin(admin.ModelAdmin):
    list_display = ("review", "text", "author", "pub_date",)
    search_fields = ("text",)
    empty_value_display = "-пусто-"


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "text", "author", "score", "pub_date",)
    search_fields = ("text",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)
