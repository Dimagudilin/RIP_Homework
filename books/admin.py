from django.contrib import admin

# Register your models here.
from books.models import Book, Comment


# отображение полей в списке объектов
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'author','image')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Book, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'body')
    raw_id_fields = ('book', 'name')


admin.site.register(Comment, CommentAdmin)
