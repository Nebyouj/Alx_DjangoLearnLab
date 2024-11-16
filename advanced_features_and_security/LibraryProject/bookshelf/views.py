from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Genre
from .forms import BookForm  # Assuming you have a form to handle book creation and editing
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    else:
        books = []
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})


# View all books
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'book_list.html', {'books': books})

# View details of a specific book
def view_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'view_book.html', {'book': book})

# Create a new book
@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after successful creation
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

# Edit an existing book
@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view_book', id=id)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# Delete a book
@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')
