

from django.urls import path
from .views import BookCreateView, BookDeleteView,BookUpdateView,BookDetailView,BookListView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List of all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Single book detail
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete book
]
