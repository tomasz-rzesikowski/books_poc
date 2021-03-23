from django.test import TestCase

from books.models import Author, PublicationLanguage, Book


class AuthorTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            name="test name"
        )

    def test_author_creation(self):
        self.assertTrue(isinstance(self.author, Author))
        self.assertEqual(f"{self.author.name}", "test name")
        self.assertEqual(self.author.__str__(), self.author.name)

    def test_author_fields(self):
        self.assertEqual(
            [*self.author.__dict__],
            ["_state", "id", "name"]
        )


class PublicationLanguageTest(TestCase):

    def setUp(self):
        self.publication_language = PublicationLanguage.objects.create(
            language="test"
        )

    def test_publication_language_creation(self):
        self.assertTrue(isinstance(self.publication_language, PublicationLanguage))
        self.assertEqual(f"{self.publication_language.language}", "test")
        self.assertEqual(self.publication_language.__str__(), self.publication_language.language)

    def test_publication_language_fields(self):
        self.assertEqual(
            [*self.publication_language.__dict__],
            ["_state", "id", "language"]
        )


class BookTest(TestCase):

    def setUp(self):
        self.publication_language = PublicationLanguage.objects.create(
            language="test"
        )
        self.book = Book.objects.create(
            id=1,
            isbn=1234567891234,
            title="test title",
            publication_year=1650,
            page_count=600,
            cover="https://www.test.com/",
            publication_language=self.publication_language
        )

    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(self.book.isbn, 1234567891234)
        self.assertEqual(f"{self.book.title}", "test title")
        self.assertEqual(self.book.publication_year, 1650)
        self.assertEqual(self.book.page_count, 600)
        self.assertEqual(f"{self.book.cover}", "https://www.test.com/")
        self.assertEqual(self.book.__str__(), f"Book \"{self.book.title}\". ISBN: {self.book.isbn}")

    def test_book_fields(self):
        self.assertEqual(
            [*self.book.__dict__],
            [
                "_state",
                "id",
                "isbn",
                "title",
                "publication_year",
                "page_count",
                "cover",
                "imported_id",
                "publication_language_id"
            ]
        )

    def test_book_fields_verbose_names(self):
        self.assertEqual(self.book._meta.get_field("isbn").verbose_name, "ISBN")
        self.assertEqual(self.book._meta.get_field("cover").verbose_name, "Cover URL")

    def test_book_fields_help_text(self):
        self.assertEqual(self.book._meta.get_field("author").help_text,
                         "If there are no author you are looking for, you can create it bellow.")
        self.assertEqual(self.book._meta.get_field("publication_language").help_text,
                         "If there are no language you are looking for, you can create it bellow.")