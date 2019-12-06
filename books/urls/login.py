from django.conf.urls import url
from django.contrib.auth import login, logout

from books import views
from books.views import user_login

urlpatterns = [
    # post views
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^$', views.dashboard, name='dashboard'),
]