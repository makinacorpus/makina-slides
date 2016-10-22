from django.test import TestCase
from django.contrib.auth.models import User


class HomepageTest(TestCase):

    def test_get_root(self):
        response = self.client.get("/")
        self.assertContains(response, "todo")


def create_user():
    return User.objects.create_user(
        username="john", password="123456", first_name="John",
        last_name="Smith")


class LoginTest(TestCase):

    def test_login_form(self):
        response = self.client.get("/login/")
        self.assertContains(response, "Password")

    def test_login_failure(self):
        response = self.client.post('/login/', {
            'username': 'john', 'password': 'wrong password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Se connecter")

    def test_login_success(self):
        create_user()
        response = self.login()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Smith")

    def test_logout(self):
        create_user()
        self.login()
        response = self.client.get('/logout/', follow=True)
        self.assertNotContains(response, "John Smith")

    def login(self):
        return self.client.post('/login/', {
            'username': 'john', 'password': '123456'
        }, follow=True)
