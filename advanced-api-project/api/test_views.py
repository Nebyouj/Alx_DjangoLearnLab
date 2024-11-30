from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create test data
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', publication_year='2023-01-01', author=self.author)

        # Define API endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
    def test_create_book(self):
        """Test creating a new book."""
        data = {
            'title': 'New Book',
            'publication_year': '2023-05-01',
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_get_book_list(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book created in setup

    def test_get_book_detail(self):
        """Test retrieving a single book's details."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        """Test updating a book."""
        data = {'title': 'Updated Book'}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book')

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(self.list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(self.list_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        Book.objects.create(title='Old Book', publication_year='2000-01-01', author=self.author)
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Old Book')
    def test_unauthenticated_user_cannot_create_book(self):

        """Test that unauthenticated users cannot create books."""
        self.client.logout()
        data = {
            'title': 'Unauthorized Book',
            'publication_year': '2023-05-01',
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
