from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField(required=False)
    cc_myself = forms.BooleanField(required=False)
