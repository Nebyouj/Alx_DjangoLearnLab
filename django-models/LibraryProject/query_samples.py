
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(f"{book.title} by {book.author.name}")

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"{book.title} by {book.author.name}")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"The librarian for {library.name} is {librarian.name}")

# Example calls
if __name__ == '__main__':
    # Query all books by a specific author
    print("Books by Author John Doe:")
    books_by_author("John Doe")

    # List all books in a library
    print("\nBooks in Central Library:")
    books_in_library("Central Library")

    # Retrieve the librarian for a library
    print("\nLibrarian for Central Library:")
    librarian_for_library("Central Library")
