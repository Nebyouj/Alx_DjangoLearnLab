from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'number_in_stock', 'daily_rate', 'genre']

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100)