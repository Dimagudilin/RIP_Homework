from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    STATUS_CHOICES = (
        ('o', 'Opened'),
        ('c', 'Closed'),
    )
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # Название
    title = models.CharField(max_length=250)
    # Для URL
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # Автор
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.PROTECT)
    # Описание
    desc = models.TextField()
    # Дата публикации
    publish = models.DateTimeField(default=timezone.now)
    # Дата выставления на форум
    created = models.DateTimeField(auto_now_add=True)
    # Последний отзыв
    updated = models.DateTimeField(auto_now=True)
    # Статус обсуждения: закрыт/Открыт
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


class Meta:
    # Метод сортировки
    ordering = ('-publish',)


def __str__(self):
    # Стандартное представление объекта
    return self.title
