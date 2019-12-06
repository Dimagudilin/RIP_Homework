from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import CommentForm, LoginForm
from .models import Book


@login_required
def dashboard(request):
    return render(request, 'list.html', {'section': 'dashboard'})


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


def user_login(request):
    # При получении user_login вызывается get
    print(request.method)
    if request.method == 'POST':
        # Создаем форму, при отправке данных
        form = LoginForm(request.POST)
        # Проверяется валидность формы (заполнение полей)
        if form.is_valid():
            cd = form.cleaned_data
            # Ищем пользователя в бд в User
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                # Проверяем активность пользователя
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'list.html', {'form': form})
