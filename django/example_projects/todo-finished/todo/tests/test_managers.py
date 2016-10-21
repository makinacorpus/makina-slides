from datetime import datetime, timedelta
from django.test import TestCase

from todo.factories import TaskFactory
from todo.models import Task


class TaskManagerTest(TestCase):

    def test_get_urgent(self):
        now = datetime.now()
        t1 = TaskFactory(
            done=False,
            deadline=now+timedelta(5))
        # Noisy
        TaskFactory(
            done=True,
            deadline=now+timedelta(5))
        TaskFactory(
            done=False,
            deadline=now+timedelta(8))

        qs = Task.objects.get_urgent()
        self.assertQuerysetEqual(qs, [repr(t1)])
