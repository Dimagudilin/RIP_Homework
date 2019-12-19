from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    author = models.CharField(max_length=250)
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
    # Картинка
    image = models.ImageField(upload_to='books/%Y/%m/%d', blank=True)


class Meta:
    # Метод сортировки
    ordering = ('-publish',)


def __str__(self):
    # Стандартное представление объекта
    return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    imagin = models.ImageField(upload_to='books/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.book)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to='books/%Y/%m/%d', blank=True, default='books/default.png')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)