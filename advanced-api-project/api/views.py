from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework


class BookListView(generics.ListAPIView):
    """
    Retrieves all books from the database.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        #queryset = Book.objects.all()
        author=self.request.author  #query_params.get('author', None)
        return Book.objects.filter(Book=author)
       # if author: 
        #    queryset = queryset.filter(author_name=author)
         #   return queryset





class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books with support for filtering by title, author, and publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework]
    filtering_fields = ['title', 'author', 'publication_year']


class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books with support for filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fileds = ['title', 'author']


class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books with support for filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']


class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books with advanced query capabilities:
    - Filter by title, author, and publication_year.
    - Search by title or author name.
    - Order by title or publication_year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_filter = ['title', 'name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']