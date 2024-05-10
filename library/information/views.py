from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')
    
class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_details.html'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    template_name = 'authors/author_form.html'

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    template_name = 'authors/author_form.html'

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')
    template_name = 'authors/author_confirm_delete.html'

# BOOKS

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    template_name = 'books/book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    template_name = 'books/book_form.html'

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'books/book_confirm_delete.html'