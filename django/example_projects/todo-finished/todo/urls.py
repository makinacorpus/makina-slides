from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^task_list/$', views.TaskList.as_view(), name='task_list'),
    url(r'^task_search/$', views.task_search, name='task_search'),
    url(r'^task/(?P<pk>\d+)/detail/$', views.TaskDetail.as_view(), name='task_detail'), # Solution 1
    #url(r'^task/(?P<identifiant>\d+)/detail/$', 'task_detail', name='task_detail'), # Solution 2
    # url(r'^add_task/$', views.AddTask.as_view(), name='add_task'), # Solution 1
    url(r'^add_task/$', views.add_task, name='add_task'), # Solution 2
    #url(r'^task/(?P<pk>\d+)/edit/$', views.EditTask.as_view(), name='edit_task'), # Solution 1
    url(r'^task/(?P<pk>\d+)/edit/$', views.edit_task, name='edit_task'), # Solution 2

    url(r'^todolist_list/$', views.TodoListList.as_view(), name='todolist_list'),
    url(r'^todolist/(?P<pk>\d+)/detail/$', views.TodoListDetail.as_view(), name='todolist_detail'),
]
