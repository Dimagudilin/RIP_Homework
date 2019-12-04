from django.shortcuts import render, get_object_or_404
from .models import Book




def book_detail(request,ident):
    book = get_object_or_404(Book, id=ident)
    return render(request, 'detail.html', {'book': book})

def book_list(request):
    # Отображение
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})



