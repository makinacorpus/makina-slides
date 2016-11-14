from datetime import date

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse

from todo.models import Task, TodoList
from todo.forms import AddTaskForm, EditTaskForm, TaskSearchForm

# --- Lists --------------------------------------------------------------------


class TodoListList(ListView):
    model = TodoList


class TaskList(ListView):
    model = Task


# --- TodoList detail ----------------------------------------------------------


class TodoListDetail(DetailView):
    model = TodoList

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['tasks'] = self.object.tasks.all()
        return context


# --- Task detail --------------------------------------------------------------


# Solution 1 : class based view
class TaskDetail(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['today'] = date.today()
        return context


# Solution 2 : function based view
def task_detail(request, identifiant):

    task = Task.objects.get(pk=identifiant)

    return render(
        request,
        'todo/task_detail.html',
        {
            'task': task,
            'today': date.today()
        })


# --- Add a task ---------------------------------------------------------------

# Solution 1: class based view
class AddTask(CreateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'todo/add_task.html'

    def get_success_url(self):
        return reverse('task_detail', args=(self.object.pk, ))


# Solution 2 : function based view
@permission_required("todo.add_task")
def add_task(request):
    form = AddTaskForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        return redirect(
            reverse(
                'task_detail',
                args=(task.pk, ))
        )
    return render(
        request,
        'todo/add_task.html',
        {
            'form': form,
        })

# --- Edit a task --------------------------------------------------------------


# Solution 1: class based view
class EditTask(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'todo/edit_task.html'

    def get_success_url(self):
        return reverse('task_detail', args=(self.object.pk, ))


# Solution 2 : function based view
@permission_required("todo.change_task")
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = EditTaskForm(request.POST or None, instance=task)
    if form.is_valid():
        task = form.save()
        return redirect(
            reverse(
                'task_detail',
                args=(task.pk, ))
        )
    return render(
        request,
        'todo/edit_task.html',
        {
            'task': task,
            'form': form,
        })


# --- Task search --------------------------------------------------------------

def task_search(request):

    form = TaskSearchForm(request.POST or None)

    tasks = Task.objects.all()
    if form.is_valid():

        name = form.cleaned_data.get('name')
        if name is not None:
            tasks = tasks.filter(name__icontains=name)

        deadline = form.cleaned_data.get('deadline')
        if deadline is not None:
            tasks = tasks.filter(deadline__lte=deadline)

        done = form.cleaned_data.get('done', None)
        if done is not None:
            tasks = tasks.filter(done=done)

    return render(
        request,
        'todo/task_search.html',
        {
            'tasks': tasks,
            'form': form,
        })
