from django.db import models

# Create your models here.

class Author_Model(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Book_Model(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author_Model, on_delete = models.CASCADE, related_name = "book_models")

    def __str__(self):
        return self.title
    

class Library_Model(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book_Model,related_name="library_models")

    def __str__(self):
        return self.name
    

class Librarian_model(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library_Model, on_delete=models.CASCADE, related_name="librarian_models")

    def __str__(self):
        return self.name