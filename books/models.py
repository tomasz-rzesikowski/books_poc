from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models


def on_language_delete():
    return PublicationLanguage.objects.get_or_create(language="unknown")[0]


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, default=None, unique=True)

    def __str__(self):
        return f"{self.name}"


class PublicationLanguage(models.Model):
    language = models.CharField(max_length=50, unique=True, null=False, default=None)

    def __str__(self):
        return f"{self.language}"


class Book(models.Model):
    isbn = models.CharField(validators=[
        RegexValidator(regex=r"(\d{12}[0-9X]{1})",
                       message="ISBN has to consists of 13 numbers or 12 numbers and \"X\"")
    ], max_length=13, unique=True, verbose_name="ISBN", null=True)

    title = models.CharField(max_length=255, null=False)
    author = models.ManyToManyField("Author",
                                    help_text="If there are no author you are looking for, you can crete it bellow.")
    publication_year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2025)], null=False)
    page_count = models.PositiveIntegerField(validators=[MaxValueValidator(9999)], null=False)
    cover = models.URLField(max_length=300, verbose_name="Cover URL")
    imported_id = models.CharField(max_length=255, null=True, unique=True)

    publication_language = models.ForeignKey(
        "PublicationLanguage",
        on_delete=models.SET(on_language_delete),
        help_text="If there are no language you are looking for, you can crete it bellow.")

    def __str__(self):
        return f"Book \"{self.title}\". ISBN: {self.isbn}"
