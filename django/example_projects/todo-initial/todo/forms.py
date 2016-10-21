from django import forms
from todo.models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('done', )


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = []


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    deadline = forms.DateField(required=False)
    done = forms.NullBooleanField(required=False)
