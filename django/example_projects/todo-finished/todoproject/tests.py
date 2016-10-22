from django.test import TestCase
from django.contrib.auth.models import User


class HomepageTest(TestCase):

    def test_get_root(self):
        response = self.client.get("/")
        self.assertContains(response, "todo")


class LoginTest(TestCase):

    def test_login_form(self):
        response = self.client.get("/login/")
        self.assertContains(response, "Password")

    def test_login_failure(self):
        response = self.client.post('/login/', {
            'username': 'john', 'password': 'smith'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "try again")

    def test_login_success(self):
        User.objects.create_user(username="john", password="123456",
                                 first_name="John", last_name="Smith")
        response = self.client.post('/login/', {
            'username': 'john', 'password': '123456'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Smith")
