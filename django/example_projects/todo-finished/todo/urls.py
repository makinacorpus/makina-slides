from rest_framework import routers

from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static

from todo.views import (
    TodoListList, TaskList, TaskDetail, AddTask, EditTask,
    TodoListDetail, TodoListViewSet, TaskViewSet)


router = routers.DefaultRouter()
router.register(r'todolists', TodoListViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = patterns(
    'todo.views',
    url(r'^', include(router.urls)),
    url(r'^task_list/$', 'task_list', name='task_list'),
    url(r'^task_search/$', 'task_search', name='task_search'),
    url(r'^task/(?P<pk>\d+)/detail/$', TaskDetail.as_view(), name='task_detail'), # Solution 1
    #url(r'^task/(?P<identifiant>\d+)/detail/$', 'task_detail', name='task_detail'), # Solution 2
    url(r'^add_task/$', AddTask.as_view(), name='add_task'), # Solution 1
    #url(r'^add_task$', 'add_task', name='add_task'), # Solution 2
    #url(r'^task/(?P<pk>\d+)/edit/$', EditTask.as_view(), name='edit_task'), # Solution 1
    url(r'^task/(?P<pk>\d+)/edit/$', 'edit_task', name='edit_task'), # Solution 2

    url(r'^todolist_list/$', TodoListList.as_view(), name='todolist_list'),
    url(r'^todolist/(?P<pk>\d+)/detail/$', TodoListDetail.as_view(), name='todolist_detail'),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
