from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import CommentForm
from .models import Book


def book_detail(request, ident):
    # Получаем книгу по id
    book = get_object_or_404(Book, id=ident)
    # Только активные комментарии
    comments = book.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.book = book
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'detail.html', {'book': book, 'comments': comments, 'comment_form': comment_form})


class BookListView(ListView):
    queryset = Book.objects.all()
    # Контекстная переменная (на странице)
    context_object_name = 'books'
    # Количество книг на странице
    paginate_by = 4
    # Название шаблона
    template_name = 'list.html'
