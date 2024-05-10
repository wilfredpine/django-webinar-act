from django import forms
from .models import Book, Author

class AuthorForm(forms.ModelForm):
    name = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
        )
    birth_date = forms.DateField(
            widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'})
        )
    biography = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
        )
    
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'biography']

class BookForm(forms.ModelForm):
    title = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
        )
    publication_year = forms.IntegerField(
            widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'})
        )
    isbn = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
        )
    author = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
            widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'})
        )
    
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'isbn', 'author']