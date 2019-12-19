from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include

from books import views

namespace ='books'
app_name ='books'

urlpatterns = [
    # post views
    # url(r'^$', views.book_list, name='book_list'),
    url(r'^$', views.BookListView.as_view(), name='book_list'),
    url(r'^(?P<ident>\w+)/$',
        views.book_detail,
        name='book_detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
