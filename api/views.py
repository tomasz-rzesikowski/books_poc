from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.serializers import BookSerializer, NameSerializer
from books.models import Book, Author


class BookList(generics.ListAPIView):
    """
        List books. Search is performed in title, author name and in publication language.
        Filter is done by publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = {
        "publication_year": ["gte", "lte"]
    }

    search_fields = ["title", "author__name", "publication_language__language"]


class AuthorList(generics.ListAPIView):
    serializer_class = NameSerializer

    def get_queryset(self):
        name = self.kwargs.get('name')
        queryset = Author.objects.filter(name__icontains=name)
        return queryset
