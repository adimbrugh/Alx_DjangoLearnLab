

from relationship_app.models import Author_Model, Book_Model, Library_Model, Librarian_model

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author_Model.objects.get(name = author_name)
        books = Book_Model.objects.filter(author = author)
        return books
    except Author_Model.DoesNotExist:
        return []
    

# List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library_Model.objects.get(name = library_name)
        return library.books.all()
    except (Library_Model.DoesNotExist):
        return []
    

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library_Model.objects.get(name = library_name)
        return Librarian_model.library
    except (Library_Model.DoesNotExist, Librarian_model.DoesNotExist):
        return None