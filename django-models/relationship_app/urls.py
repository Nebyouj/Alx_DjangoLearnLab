from django.urls import path
from relationship_app.views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # For the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # For the class-based view
]