# Generated by Django 3.1.7 on 2021-03-23 15:27

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_change_import_id_in_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(
                help_text='If there are no author you are looking for, you can create it bellow.',
                to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_language',
            field=models.ForeignKey(
                help_text='If there are no language you are looking for, you can create it bellow.',
                on_delete=models.SET(books.models.on_language_delete),
                to='books.publicationlanguage'),
        ),
    ]
