from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .models import Book


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer