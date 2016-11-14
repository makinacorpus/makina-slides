from django.conf.urls import url
from library import views


urlpatterns = [
    url('recent/$', views.recent_books, name='recent'),
    url('book/(?P<book_id>.+)/$', views.book_detail,
        name='detail')
]
