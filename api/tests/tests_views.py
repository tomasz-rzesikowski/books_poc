from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import BookSerializer
from books.models import Book, PublicationLanguage, Author
from django.test import Client

client = Client()


class TestBookList(APITestCase):
    def setUp(self) -> None:
        self.publication_language_id = PublicationLanguage.objects.get_or_create(
            language="en")[0]
        self.author_id = Author.objects.get_or_create(name="test_author")[0]

    def test_empty_list_books(self):
        response = client.get(reverse("api:book_list"))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_books(self):
        book = Book.objects.create(
            isbn="1234567891234",
            title="test_title",
            publication_year=2008,
            page_count=1000,
            cover="https://google.pl",
            publication_language=self.publication_language_id)
        book.author.set([self.author_id])

        response = client.get(reverse("api:book_list"))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_publication_date(self):
        book_first = Book.objects.create(
            isbn="1234567891234",
            title="test_title",
            publication_year=2008,
            page_count=2008,
            cover="https://google.pl",
            publication_language=self.publication_language_id)
        book_first.author.set([self.author_id])

        book_second = Book.objects.create(
            isbn="1234567891235",
            title="test_title123",
            publication_year=2018,
            page_count=2008,
            cover="https://google.pl",
            publication_language=self.publication_language_id)
        book_second.author.set([self.author_id])

        url = f"{reverse('api:book_list')}?publication_year__gte=&publication_year__lte=2013"
        response = client.get(url)
        books = Book.objects.filter(publication_year__lte=2013)
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
