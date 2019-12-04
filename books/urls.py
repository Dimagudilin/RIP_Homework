from django.conf.urls import url

from . import views

namespace ='books'
app_name ='books'

urlpatterns = [
    # post views
    url(r'^$', views.book_list, name='book_list'),
    url(r'^(?P<ident>\w+)/$',
        views.book_detail,
        name='book_detail'),
]