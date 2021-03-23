from django.test import TestCase
from django.urls import reverse, resolve

from books.models import PublicationLanguage, Author, Book
from books.views import ListImportView


class ListBookViewTest(TestCase):
    def setUp(self):
        url = reverse("books:list-books")
        self.response = self.client.get(url)
        test_language = PublicationLanguage.objects.create(language="en")
        test_author = Author.objects.create(name="Tester")
        test_book = Book.objects.create(isbn="1234567890123",
                                        title="test",
                                        publication_year="2010",
                                        page_count="500",
                                        cover="https://applover.pl/wp-content/uploads/2020/01/"
                                              "kisspng-python-computer-icons-programming-language-executa"
                                              "-5d0f0aa7c78fb3.0414836115612668558174-1024x1024.png",
                                        imported_id=1,
                                        publication_language=test_language
                                        )
        test_book2 = Book.objects.create(isbn="2234567890123",
                                         title="test2",
                                         publication_year="2011",
                                         page_count="540",
                                         cover="https://applover.pl/wp-content/uploads/2020/01/"
                                               "kisspng-python-computer-icons-programming-language-executa"
                                               "-5d0f0aa7c78fb3.0414836115612668558174-1024x1024.png",
                                         imported_id=2,
                                         publication_language=test_language
                                         )
        test_book.author.add(test_author)
        test_book2.author.add(test_author)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_name(self):
        self.assertTemplateUsed(self.response, "books/books.html")

    def test_contain_correct_html(self):
        self.assertContains(self.response, "have what you looking for.")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hello! You should not see that")


class ListImportViewTests(TestCase):

    def setUp(self):
        url = reverse("books:list-import-books")
        self.response = self.client.get(url)

    def test_list_import_view_get_url_name(self):
        self.assertEqual(self.client.get(reverse("books:list-import-books"))
                         .status_code, 200)
        self.assertEqual(self.response.status_code, 200)

    def test_list_import_view_post_url_name(self):
        response = self.client.post(reverse("books:list-import-books"))
        self.assertEqual(response.status_code, 405)

    def test_list_import_view_template(self):
        self.assertTemplateUsed(self.response, "books/import_books.html")
        self.assertContains(self.response, "Search and Import")
        self.assertNotContains(self.response, "Create Book")

    def test_import_books(self):
        self.assertContains(self.response, "csrf")

    def test_list_import_view(self):
        view = resolve("/books/import_books/")
        self.assertEqual(view.func.__name__, ListImportView.as_view().__name__)
