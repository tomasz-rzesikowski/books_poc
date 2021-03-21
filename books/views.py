from django.views.generic import ListView

from books.models import Book


class BookListView(ListView):
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
