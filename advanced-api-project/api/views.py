from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


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