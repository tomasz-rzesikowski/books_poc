from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "isbn", "title", "author", "publication_year", "page_count", "cover", "publication_language")
        depth = 1
