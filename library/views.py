from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination


class BookPagination(PageNumberPagination):
    """
    BookPagination is a custom pagination class that inherits from PageNumberPagination.

    It sets the default page size to 10 and allows the page size to be changed by a query parameter.
    """
    page_size = 10
    page_size_query_param = 'page_size'


class BookViewSet(viewsets.ModelViewSet):
    """
    BookViewSet is a viewset for the Book model.

    It uses the BookSerializer to serialize and deserialize the Book model instances.
    It uses the BookPagination class to paginate the results.
    It allows filtering the results by the 'author', 'published_date', and 'language' fields.

    The queryset includes all Book instances, ordered by their 'id'.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'published_date', 'language']
