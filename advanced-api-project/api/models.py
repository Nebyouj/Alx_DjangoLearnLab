from django.db import models
from django.utils import timezone

# Author model represents an individual author in the system.
# Each author has a unique name.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name

# Book model represents a book in the system.
# Each book is associated with a single author through a ForeignKey relationship.
class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book
    publication_year = models.DateField(default=timezone.now)  # Publication date of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Foreign key linking to the Author model

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    # Additional validation can be added here to enforce model-level constraints if necessary.

