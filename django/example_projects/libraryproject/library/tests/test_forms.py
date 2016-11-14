# tests/test_forms.py
from datetime import date
from django.test import TestCase
from library.forms import PeriodForm


class PeriodFormTest(TestCase):

    def test_init_without_begin(self):
        f = PeriodForm()
        self.assertIsNone(f.initial.get('end'))

    def test_init_with_begin(self):
        initial = {'begin': date(2014, 1, 1)}
        f = PeriodForm(initial=initial)
        self.assertEqual(f.initial.get('begin'), date(2014, 1, 1))
        self.assertEqual(f.initial.get('end'), date(2014, 2, 1))
