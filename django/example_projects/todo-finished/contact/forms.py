from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField(required=False)
    cc_myself = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('subject'):
            self.initial['subject'] = "Réclamation"

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        cc_myself = cleaned_data.get("cc_myself")
        sender = cleaned_data.get("sender")

        if cc_myself and not sender:
            raise forms.ValidationError(
                "Veuillez donner votre adresse email pour "
                "recevoir une copie du message"
            )
