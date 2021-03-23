import requests
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from books.models import Book, Author, PublicationLanguage


class ListBookView(ListView):
    model = Book
    template_name = "books/books.html"
    context_object_name = "books"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q')
        gte = self.request.GET.get('gte') if self.request.GET.get('gte') else 0
        lte = self.request.GET.get('lte') if self.request.GET.get('lte') else 9999
        if query:
            title_query = self.model.objects.filter(title__icontains=query) \
                .prefetch_related("author") \
                .prefetch_related("publication_language")
            name_query = self.model.objects.filter(author__name__icontains=query)
            language_query = self.model.objects.filter(publication_language__language__icontains=query)
            object_list = title_query | name_query | language_query
        else:
            object_list = self.model.objects \
                .prefetch_related("author") \
                .prefetch_related("publication_language")
        object_list = object_list.filter(publication_year__gte=gte, publication_year__lte=lte)
        return object_list


class CreateBookView(CreateView):
    model = Book
    template_name = "books/create_book.html"
    fields = ("isbn", "title", "author", "publication_year", "page_count", "cover", "publication_language")
    raise_exception = True
    success_url = reverse_lazy('books:list-books')


class UpdateBookView(UpdateView):
    model = Book
    template_name = "books/update_book.html"
    fields = ("isbn", "title", "author", "publication_year", "page_count", "cover", "publication_language")
    raise_exception = True
    success_url = reverse_lazy('books:list-books')


class CreateAuthorView(CreateView):
    model = Author
    template_name = "books/create_author.html"
    fields = ("name",)
    raise_exception = True
    success_url = reverse_lazy('books:create-book')


class CreateLanguageView(CreateView):
    model = PublicationLanguage
    template_name = "books/create_pub_lang.html"
    fields = ("language",)
    raise_exception = True
    success_url = reverse_lazy('books:create-book')


class ListImportView(ListView):
    template_name = "books/import_books.html"
    context_object_name = "books"

    def get_queryset(self):
        query = self.request.GET.get('s')
        if query:
            import_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
            return self.get_books_from_import(import_url)
        return []

    def get_books_from_import(self, import_url):
        imported_data = requests.get(import_url)
        imported_books = []
        for obj in imported_data.json()["items"]:
            imported_id = obj["id"]
            volume_info = obj.get("volumeInfo", {})
            if not volume_info:
                return False
            industry_identifiers = volume_info.get("industryIdentifiers", "")
            isbn = None
            for i in industry_identifiers:
                if i.get("type") == "ISBN_13":
                    isbn = i.get("identifier")
            title = volume_info.get("title", "")
            authors = []
            for a in volume_info.get("authors", ""):
                authors.append(a)
            publication_year = volume_info.get("publishedDate", "")[:4]
            page_count = volume_info.get("pageCount", 0)
            cover = volume_info.get("imageLinks", {}).get("thumbnail", "")
            publication_language = volume_info.get("language", "")
            imported_book = {
                "isbn": isbn,
                "title": title,
                "authors": authors,
                "publication_year": publication_year,
                "page_count": page_count,
                "cover": cover,
                "publication_language": publication_language,
                "imported_id": imported_id
            }
            imported_books.append(imported_book)
        self.save_imported_books(imported_books)
        return imported_books

    @staticmethod
    def save_imported_books(imported_books):
        for imported_book in imported_books:
            try:
                book = Book.objects.create(
                    isbn=imported_book["isbn"],
                    title=imported_book["title"],
                    publication_year=imported_book["publication_year"],
                    page_count=imported_book["page_count"],
                    cover=imported_book["cover"],
                    imported_id=imported_book["imported_id"]
                )
                publication_language = PublicationLanguage.objects.get_or_create(
                    language=imported_book["publication_language"]
                )[0]
                book.publication_language.set(publication_language)
                authors = []
                for a in imported_book["authors"]:
                    authors.append(Author.objects.get_or_create(name=a)[0])
                book.author.set(authors)
            except IntegrityError:
                pass
