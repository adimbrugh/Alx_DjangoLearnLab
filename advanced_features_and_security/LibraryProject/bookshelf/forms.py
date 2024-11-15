from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100, 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search by title'})
    )


