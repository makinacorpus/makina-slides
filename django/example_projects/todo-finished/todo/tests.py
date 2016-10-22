from datetime import timedelta
from django.test import TestCase
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
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


class TestUrgentManager(TestCase):

    def test_no_task(self):
        self.assertEqual(Task.objects.get_urgent().count(), 0)

    def test_three_tasks_with_one_urgent(self):
        now = timezone.now()
        todo_list = TodoList.objects.create(label="Testing list")
        Task.objects.create(name="Not urgent",
                            deadline=now + timedelta(days=10),
                            todo_list=todo_list)
        Task.objects.create(name="Urgent but done",
                            deadline=now + timedelta(days=10),
                            todo_list=todo_list,
                            done=True)
        Task.objects.create(name="Urgent and not done",
                            deadline=now + timedelta(days=2),
                            todo_list=todo_list)
        self.assertEqual(Task.objects.get_urgent().count(), 1)


class TestDates(TestCase):

    def test_modification_date_after_a_change(self):
        todo_list = TodoList.objects.create(label="Testing list")
        Task.objects.create(name="A task", todo_list=todo_list)
        task = Task.objects.first()
        task.name = "New name"
        task.save()
        self.assertGreater(task.modification_time, task.creation_time)
