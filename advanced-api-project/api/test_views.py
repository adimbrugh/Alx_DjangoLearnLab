

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book
#from api.serializers import BookSerializer


class BookAPITests(APITestCase):
    """
    Test suite for Book model API endpoints.
    """
    def setUp(self):
        #create a test user
        self.user = User.objects.create_user(username='testuser', password='testuser')

        #create an author
        self.author = Author.objects.create(name='J.K. Rowlig')

        #create books
        self.book1 = Book.objects.create(
            title = "Harry Potter and the sorcerer",
            publication_year = 1997,
            author = self.author
        )

        self.book2 = Book.objects.create(
            title = "Harry Potter and Chamber of Secrets",
            publication_year = 1998,
            author= self.author
        )

        #authentication setup
        self.client.login(username = 'testuser', password = 'testpassword')



    def test_create_book(self):
        
        #Test if a book can be created successfully.
        url = "/api/books/"
        data = {
        "title": "Harry Potter and the Prisoner of Azkaban",
        "publication_year": 1999,
        "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Harry Potter and the Prisoner of Azkaban")



    def test_get_book(self):
        url = f"/api/books/{self.book1.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)


    def test_update_book(self):
        url = f"/api/books/{self.book1.id}/"
        data = {"title": "Harry Potter and the Philosopher's Stone"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter and the Philosopher's Stone")


    def test_delete_book(self):
        url = f"/api/books/{self.book1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())


    def test_filter_books_by_title(self):
        url = "/api/books/?title=Harry Potter and the Sorcerer's Stone"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_search_books_by_author(self):
        url = "/api/books/?search=J.K. Rowling"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)
