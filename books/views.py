import requests
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, FormView

from books.forms import ImportForm
from books.models import Book, Author, PublicationLanguage


class ListBookView(ListView):
    model = Book
    template_name = "books/books.html"
    context_object_name = "books"

    def get_queryset(self):
        query = self.request.GET.get('q')
        gte = self.request.GET.get('gte') if self.request.GET.get('gte') else 0
        lte = self.request.GET.get('lte') if self.request.GET.get('lte') else 9999

        if query:
            title_query = self.model.objects.filter(title__icontains=query)
            name_query = self.model.objects.filter(author__name__icontains=query)
            language_query = self.model.objects.filter(publication_language__language__icontains=query)
            object_list = title_query | name_query | language_query
        else:
            object_list = self.model.objects.prefetch_related("author")

        if gte or lte:
            object_list = object_list.filter(publication_year__gte=gte, publication_year__lte=lte)

        if lte:
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


class ImportView(FormView):
    form_class = ImportForm
    template_name = "books/import_books.html"
    success_url = reverse_lazy('books:list-books')

    def form_valid(self, form):
        import_url = form.cleaned_data["import_url"]
        self.create_books_from_import(import_url=import_url)

        return super().form_valid(form)

    def create_books_from_import(self, import_url):
        imported_data = requests.get(import_url)

        books = []

        for obj in imported_data.json()["items"]:
            volume_info = obj["volumeInfo"]
            industry_identifiers = volume_info["industryIdentifiers"]

            isbn = ""
            for i in industry_identifiers:
                if i["type"] == "ISBN_13":
                    isbn = i["identifier"]

            title = volume_info["title"]

            authors = []
            for a in volume_info["authors"]:
                authors.append(Author.objects.get_or_create(name=a)[0])

            publication_year = volume_info["publishedDate"][:4]
            page_count = volume_info.get("pageCount", "0")
            cover = volume_info.get("imageLinks", "").get("thumbnail", "")
            publication_language = volume_info["language"]

            try:
                book = Book.objects.create(
                    isbn=isbn,
                    title=title,
                    publication_year=publication_year,
                    page_count=page_count,
                    cover=cover,
                    publication_language=PublicationLanguage.objects.get_or_create(language=publication_language)[0]
                )

                book.author.set(authors)
                books.append(book)
            except IntegrityError:
                pass
