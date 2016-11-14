import mock

from todo.factories import TaskFactory
from todo.models import TaskManager
from django_webtest import WebTest

from pyquery import PyQuery as pq

from django.core.urlresolvers import reverse


class TaskViewsTest(WebTest):

    @mock.patch.object(TaskManager, 'get_urgent')
    def test_task_list(self, mock_get_urgent):
        url = reverse('task_list')

        # With values
        mock_get_urgent.return_value = [TaskFactory(name='toto')]
        resp = self.app.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('toto', resp.content)

        # Without values
        mock_get_urgent.return_value = []
        resp = self.app.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('No task', resp.content)

        self.assertEqual(len(pq('.red', resp.content)), 1)

        #self.assertTrue(mock_get_urgent.called)
