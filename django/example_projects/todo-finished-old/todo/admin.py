from django.contrib import admin
from todo.models import Task, TodoList

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'deadline', 'done']
    list_filter = ['todo_list', 'done']
    date_hierarchy = 'deadline'
    search_fields = ['name', 'descritpion', 'todo_list__label']

admin.site.register(TodoList)
admin.site.register(Task, TaskAdmin)
