from django.shortcuts import render
from .models import Book


from django.views.generic import (
    CreateView, 
    ListView, 
    UpdateView, 
    DetailView, 
    DeleteView
)

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

class BookListView(ListView):
    #queryset = Book.objects.filter(user=request.user)
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"