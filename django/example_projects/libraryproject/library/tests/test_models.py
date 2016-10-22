from django.test import TestCase
from library.models import Author


class AuthorAsStringTest(TestCase):

    def test_with_first_name(self):

        author = Author.objects.create(firstname='René',
                                       lastname='Descartes')
        self.assertEqual(str(author), 'René Descartes')

    def test_without_first_name(self):

        author = Author.objects.create(lastname='Platon')
        self.assertEqual(str(author), 'Platon')
