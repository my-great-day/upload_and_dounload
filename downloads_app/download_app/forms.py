from django.forms import forms


class Form_File(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='max 100 mb file'
    )
