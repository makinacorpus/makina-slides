from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    label = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='todo_lists')

    class Meta:
        db_table = 'todo_list'
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo lists'
        ordering = ('label', )

    def __unicode__(self):
        return self.label


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, related_name='tasks')

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ('-deadline', )

    def __unicode__(self):
        return self.name
