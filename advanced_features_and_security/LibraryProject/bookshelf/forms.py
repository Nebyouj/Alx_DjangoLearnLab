from django import forms
from .models import Book

# ExampleForm to handle some basic input
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label="Book Title")
    author = forms.CharField(max_length=100, required=True, label="Author Name")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Description")
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'number_in_stock', 'daily_rate', 'genre']

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100)