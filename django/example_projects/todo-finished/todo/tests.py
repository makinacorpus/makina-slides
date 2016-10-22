from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from .models import Task, TodoList


def create_user():
    return User.objects.create_user(username="john", password="123456")


class TestTaskAdminPermission(TestCase):

    def test_cannot_create(self):
        todo_list = TodoList.objects.create(label="Testing list")
        self.assertEqual(Task.objects.count(), 0)
        self.client.post("/todo/add_task/", {
            "name": "Test task",
            "description": "Task description",
            "deadline": "2016-10-25",
            "todo_list": todo_list.pk,
        })
        self.assertEqual(Task.objects.count(), 0)

    def test_can_create(self):
        user = create_user()
        group = Group.objects.create(name="admin")
        permission = Permission.objects.get(codename="add_task")
        group.permissions.add(permission)
        user.groups.add(group)
        todo_list = TodoList.objects.create(label="Testing list")

        self.assertEqual(Task.objects.count(), 0)

        self.client.login(username='john', password='123456')
        self.client.post("/todo/add_task/", {
            "name": "Test task",
            "description": "Task description",
            "deadline": "2016-10-25",
            "todo_list": todo_list.pk,
        })

        self.assertEqual(Task.objects.count(), 1)
