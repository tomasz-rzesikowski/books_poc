from django.contrib import admin

from books.models import Author, Book, PublicationLanguage

admin.site.register(Author)
admin.site.register(PublicationLanguage)
admin.site.register(Book)
