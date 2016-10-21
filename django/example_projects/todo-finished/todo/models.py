from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    created = models.DateField(auto_now_add=True, null=True)
    modified = models.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True


class TodoList(CommonInfo):
    label = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='todo_lists', null=True, blank=True)

    class Meta:
        db_table = 'todo_list'
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo lists'
        ordering = ('label', )

    def __unicode__(self):
        return self.label


class TaskManager(models.Manager):
    def get_urgent(self):
        now = datetime.now()
        return self.get_query_set().filter(
            done=False,
            deadline__lte=now+timedelta(7))

    def get_old(self):
        now = datetime.now()
        return self.get_query_set().filter(
            done=True,
            deadline__lte=now-timedelta(7))


class Task(CommonInfo):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    done = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, related_name='tasks')
    attachment = models.FileField(upload_to='tasks', blank=True, null=True)

    objects = TaskManager()

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ('-deadline', )
        permissions = (
            ('search_task', 'Search task'),
        )

    def __unicode__(self):
        return self.name
