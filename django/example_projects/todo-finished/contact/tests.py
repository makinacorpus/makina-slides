from django.test import TestCase


from contact.forms import ContactForm


class TestContactForm(TestCase):

    def test_subject_too_long(self):
        form = ContactForm({"subject": "X" * 200, "message": "Hello"})
        self.assertFalse(form.is_valid())

    def test_subject_ok(self):
        form = ContactForm({"subject": "X" * 100, "message": "Hello"})
        self.assertTrue(form.is_valid())

    def test_initial_subject(self):
        form = ContactForm()
        self.assertEqual(form.initial['subject'], "Réclamation")

    def test_user_supplied_subject(self):
        form = ContactForm(initial={"subject": "Mon sujet"})
        self.assertEqual(form.initial['subject'], "Mon sujet")

    def test_sender_missing_but_cc_myself_true(self):
        form = ContactForm({"subject": "Bonjour", "cc_myself": True,
                            "message": "Ça va ?"})
        self.assertFalse(form.is_valid())
