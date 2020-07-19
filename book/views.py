from django.shortcuts import render
from book.models import Book


def BookList(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context=context)
