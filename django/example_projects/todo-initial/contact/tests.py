from django.test import TestCase


from contact.forms import ContactForm


class TestContactForm(TestCase):

    def test_subject_too_long(self):
        form = ContactForm({"subject": "X" * 200, "message": "Hello"})
        self.assertFalse(form.is_valid())

    def test_subject_ok(self):
        form = ContactForm({"subject": "X" * 100, "message": "Hello"})
        self.assertTrue(form.is_valid())
