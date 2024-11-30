from django.utils import timezone
from rest_framework import serializers
from .models import Book, Author

# AuthorSerializer serializes the Author model.
# It converts the Author model instances into JSON and vice versa.
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  # Specifies the model to be serialized
        fields = ['id', 'name']  # Fields to be included in the serialized output

# BookSerializer serializes the Book model.
# It includes nested serialization for the related Author model to display author details.
class BookSerializer(serializers.ModelSerializer):
    # Nested serializer to include the author details within the book's serialized output
    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book  # Specifies the model to be serialized
        fields = ['id', 'title', 'publication_year', 'author']  # Fields to include in the serialized output

    # Field-level validation for the publication_year field.
    # Ensures that the publication year is not set in the future.
    def validate_publication_year(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    # Explanation of relationship handling:
    # The BookSerializer uses a nested AuthorSerializer to represent the Author-Book relationship.
    # This allows Book instances to display author information directly.
    # The `author` field expects an Author object, not an ID.

