from datetime import date
import factory
import factory.django

from todo import models


class TodoListFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.TodoList

    label = factory.Sequence(lambda n: 'My list %s' % n)


class TaskFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Task

    name = factory.Sequence(lambda n: 'My task %s' % n)
    description = "Task description"
    deadline = date.today()
    done = False
    todo_list = factory.SubFactory(TodoListFactory)
