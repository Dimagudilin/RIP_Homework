from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Book




def book_detail(request,ident):
    # Получаем книгу по id
    book = get_object_or_404(Book, id=ident)
    return render(request, 'detail.html', {'book': book})


class BookListView(ListView):
    queryset = Book.objects.all()
    # Контекстная переменная (на странице)
    context_object_name = 'books'
    # Количество книг на странице
    paginate_by = 4
    # Название шаблона
    template_name = 'list.html'

