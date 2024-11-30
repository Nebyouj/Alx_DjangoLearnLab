from rest_framework.exceptions import ValidationError
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books with advanced query capabilities:
    
    - Filtering by title, author name, and publication year.
    - Searching within the title and author's name fields.
    - Ordering results by title or publication year (ascending/descending).

    Query Parameters:
    
    - Filtering: ?title=TitleValue&author__name=AuthorName
    - Searching: ?search=SearchTerm
    - Ordering: ?ordering=field_name or ?ordering=-field_name for descending order
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for everyone

     # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define fields for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields for search functionality
    search_fields = ['title', 'author__name']

    # Fields for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering 
    ordering = ['title']

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for everyone


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > timezone.now().date():
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.validated_data['publication_year'] > timezone.now().date():
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only



