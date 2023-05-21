import csv
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from reviews.models import Comment, Review
from titles.models import Category, Genre, GenreTitle, Title


User = get_user_model()

FILES = {
    Category: "static/data/category.csv",
    Genre: "static/data/genre.csv",
    Title: "static/data/titles.csv",
    GenreTitle: "static/data/genre_title.csv",
    User: "static/data/users.csv",
    Review: "static/data/review.csv",
    Comment: "static/data/comments.csv",
}


class Command(BaseCommand):
    help = "Loading data from from csv to database."

    def handle(self, *args, **options):
        os.remove("./db.sqlite3")
        os.system("python manage.py migrate")
        for model, file in FILES.items():
            with open(file, encoding="utf-8-sig") as opened_file:
                parser = csv.DictReader(opened_file, delimiter=",")
                for row in parser:
                    model.objects.get_or_create(**row)
