from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.utils.translation import gettext as _
from books.forms import CommentForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from books.models import Book
from .models import Profile

# Страница отзывов
@login_required
def book_detail(request, ident):
    # Получаем книгу по id
    book = get_object_or_404(Book, id=ident)
    name = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=name)
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
            new_comment.name = name
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(request.path)
    else:
        comment_form = CommentForm()
    return render(request, 'detail.html', {'book': book, 'comments': comments, 'comment_form': comment_form})


# Список книг
class BookListView(LoginRequiredMixin, ListView):
    queryset = Book.objects.all()
    # Контекстная переменная (на странице)
    context_object_name = 'books'
    # Количество книг на странице
    paginate_by = 4
    # Название шаблона
    template_name = 'list.html'


# Форма регистрации
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'registration/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Ваш профиль был успешно обновлен!'))
            return redirect('/book/')
        else:
            raise ValidationError(_('Invalid date - renewal in past'))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})