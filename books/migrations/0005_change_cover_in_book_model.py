# Generated by Django 3.1.7 on 2021-03-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_change_isbn_in_book_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.URLField(max_length=300, verbose_name='Cover URL'),
        ),
    ]