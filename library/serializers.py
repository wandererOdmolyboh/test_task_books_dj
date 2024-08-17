from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer is a ModelSerializer for the Book model.

    This serializer automatically creates fields that correspond to the Book model fields.
    It includes all fields from the Book model ('__all__').

    When creating a new book or updating an existing one using the API, this serializer
    validates the data to ensure it fits the constraints of the Book model.
    """
    class Meta:
        model = Book
        fields = '__all__'
