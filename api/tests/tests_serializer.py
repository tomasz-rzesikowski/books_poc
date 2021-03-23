from django.test import TestCase

from api.serializers import BookSerializer
from books.models import Book, Author, PublicationLanguage


class TestBookSerializer(TestCase):
    def setUp(self) -> None:
        self.publication_language_id = PublicationLanguage.objects.get_or_create(
            language="en")[0]
        self.author_id = Author.objects.get_or_create(name="test_author")[0]

        self.book = Book.objects.create(
            isbn="1234567891234",
            title="test_title",
            publication_year=2008,
            page_count=2008,
            cover="https://google.pl",
            publication_language=self.publication_language_id)

        self.book.author.set([self.author_id])
        self.serializer_book = BookSerializer(instance=self.book)

        self.book_attributes = {
            "isbn": "1234567891234",
            "title": "test_title",
            "publication_year": 2008,
            "page_count": 2008,
            "cover": "https://google.pl",
            "publication_language": "en",
            "author": "test_author"
        }

    def test_model_fields(self):
        data = self.serializer_book.data
        self.assertEqual(data.keys(), {"id",
                                       "isbn",
                                       "title",
                                       "author",
                                       "publication_year",
                                       "page_count",
                                       "cover",
                                       "publication_language"}
                         )

    def test_fields_content(self):
        data = self.serializer_book.data
        self.assertEqual(data["isbn"], self.book_attributes["isbn"])
        self.assertEqual(data["title"], self.book_attributes["title"])
        self.assertEqual(data["publication_year"], self.book_attributes["publication_year"])
        self.assertEqual(data["page_count"], self.book_attributes["page_count"])
        self.assertEqual(data["cover"], self.book_attributes["cover"])
        self.assertEqual(data["publication_language"]["language"], self.book_attributes["publication_language"])
        self.assertEqual(data["author"][0]["name"], self.book_attributes["author"])
