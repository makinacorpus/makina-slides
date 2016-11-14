from django.contrib import admin
from todo.models import Task, TodoList


admin.site.register(TodoList)
admin.site.register(Task)
