from django.urls import path
from . import views

urlpatterns = [
    # URL for listing all books
    path('books/', views.book_list, name='book_list'),
    
    # URL for viewing details of a specific book
    path('book/<int:id>/', views.view_book, name='view_book'),
    
    # URL for creating a new book
    path('book/create/', views.create_book, name='create_book'),
    
    # URL for editing an existing book
    path('book/edit/<int:id>/', views.edit_book, name='edit_book'),
    
    # URL for deleting a book
    path('book/delete/<int:id>/', views.delete_book, name='delete_book'),
]
