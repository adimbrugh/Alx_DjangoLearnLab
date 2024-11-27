from django.db import models

# Create your models here.


# Model representing an author
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


## Model representing a book
# Each book has a title, a publication year, and an associated author
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title