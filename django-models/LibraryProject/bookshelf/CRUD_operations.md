```python
from bookshelf.models import Book

Book = Book.objects.create(title="1984",author="George Orwell",publication_year = 1949)
Book
#<Book: 1984 by George Orwell>
```

```python
from bookshelf.models import Book

Book.objects.get(id=book.id)
# <Book: 1984 by George Orwell>
```

```python
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
# <Book: Nineteen Eighty-Four by George Orwell>
```

```python
book.delete()
Book.objects.all() 
# <QuerySet []>
```