

from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")


from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
