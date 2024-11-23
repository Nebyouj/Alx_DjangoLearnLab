from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Correct attribute name (lowercase 'q')
    serializer_class = BookSerializer


