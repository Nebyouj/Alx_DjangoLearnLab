from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """
    Function to get all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        return books_by_author
    except Author.DoesNotExist:
        return f"Author with name '{author_name}' does not exist."

def get_books_in_library(library_name):
    """
    Function to get all books in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        return books_in_library
    except Library.DoesNotExist:
        return f"Library with name '{library_name}' does not exist."

def get_librarian_for_library(library_name):
    """
    Function to get the librarian for a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return f"Library with name '{library_name}' does not exist."
    except Librarian.DoesNotExist:
        return f"Librarian for library '{library_name}' does not exist."

