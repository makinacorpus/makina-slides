from django import forms


class PeriodForm(forms.Form):
    begin = forms.DateField()
    end = forms.DateField()

    def __init__(self, *args, **kwargs):
        super(PeriodForm, self).__init__(*args, **kwargs)

        begin = self.initial.get('begin', None)
        if begin:
            self.initial['end'] = begin.replace(month=begin.month + 1)
