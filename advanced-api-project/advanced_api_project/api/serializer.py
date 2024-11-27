

from rest_framework import serializers
from .models import Author, Book


# Serializer for the Book model
# Includes a custom validation method to ensure publication_year is not in the future
class BookSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    """
    Custom validation to ensure the publication year is not in the future.
    Raises a ValidationError if the year is invalid.
    """
    def validate_publication_year(self, value):
        import datetime
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the futuer.")
        return value


# Serializer for the Author model
# Includes a nested BookSerializer to serialize related books dynamically
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerilaizer(many = True, read_only = True) # Nested serializer for related books

    class Meta:
        model = Author
        fields = ('name')