from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TaskManager(models.Manager):

    def get_urgent(self):
        now = timezone.now()
        return self.get_queryset().filter(
            deadline__lte=now + timedelta(7),
            done=False)


class TodoList(models.Model):
    label = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='todo_lists')

    class Meta:
        db_table = 'todo_list'
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo lists'
        ordering = ('label', )

    def __str__(self):
        return self.label


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, related_name='tasks')

    objects = TaskManager()

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ('-deadline', )

    def __str__(self):
        return self.name
