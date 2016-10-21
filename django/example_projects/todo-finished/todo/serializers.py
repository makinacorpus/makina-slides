from rest_framework import serializers

from todo.models import TodoList, Task


class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ('label',)


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'deadline', 'done', 'todo_list')
