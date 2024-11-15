

from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Search for a book'}))
