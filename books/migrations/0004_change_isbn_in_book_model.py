# Generated by Django 3.1.7 on 2021-03-21 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_add_page_year_cover_to_book_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(
                max_length=13,
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message='ISBN has to be 13 character long.',
                        regex='(\\d{12}[0-9X]{1})'
                    )
                ],
                verbose_name='ISBN'),
            ),
        ]
