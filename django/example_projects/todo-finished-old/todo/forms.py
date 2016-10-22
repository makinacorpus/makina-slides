from datetime import date, timedelta
from django import forms
from todo.models import Task


class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('done', )

    def __init__(self, *args, **kwargs):
        super(AddTaskForm, self).__init__(*args, **kwargs)
        self.initial['deadline'] = date.today() + timedelta(7)

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline < date.today():
            msg = 'Deadline should be in future !'
            raise forms.ValidationError(msg)
        return deadline


class EditTaskForm(forms.ModelForm):

    class Meta:
        model = Task

    def clean(self):
        done = self.cleaned_data.get('done')
        deadline = self.cleaned_data.get('deadline')
        if done and deadline and deadline > date.today():
            msg = "I'm sure you didn't do this task before its deadline!"
            self.add_error("done", msg)
        return self.cleaned_data


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    deadline = forms.DateField(required=False)
    done = forms.NullBooleanField(required=False)
