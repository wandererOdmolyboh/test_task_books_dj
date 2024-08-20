from django.db import models


class Book(models.Model):
    """
    The Book model represents a book in a library.

    Fields:
        title (CharField): The title of the book. This is a required field.
        author (CharField): The author of the book. This is a required field.
        published_date (DateField): The date the book was published. This is an optional field.
        isbn (CharField): The International Standard Book Number of the book. This is a unique and required field.
        pages (IntegerField): The number of pages in the book. This is an optional field.
        cover (URLField): The URL of the book's cover image. This is an optional field.
        language (CharField): The language of the book. This is a required field.
    """

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField(null=True, blank=True)
    cover = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=2)
