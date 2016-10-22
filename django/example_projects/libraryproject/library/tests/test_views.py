# tests/test_forms.py
from datetime import date
from django.test import TestCase
from library.models import Book


class BookViewTest(TestCase):

    def test_recent_books_view(self):
        recent_date = date.today()
        recent_book = Book.objects.create(title='Titre du livre récent',
                                          published=recent_date)

        old_date = recent_date.replace(year=recent_date.year - 1)
        old_book = Book.objects.create(title='Titre du vieux livre',
                                       published=old_date)

        response = self.client.get("/library/recent/")

        self.assertNotContains(response, old_book.title)
        self.assertContains(response, recent_book.title)
