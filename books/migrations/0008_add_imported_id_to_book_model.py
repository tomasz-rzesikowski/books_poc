# Generated by Django 3.1.7 on 2021-03-22 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_change_isbn_and_page_count_in_book_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='imported_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
