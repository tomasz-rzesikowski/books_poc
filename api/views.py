from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.serializers import BookSerializer
from books.models import Book


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = {
        "publication_year": ["gte", "lte"]
    }

    search_fields = ["title", "author__name", "publication_language__language"]
