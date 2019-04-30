from typing import Type

from django import forms

from quastionsapp.models import UserContact
from .models import UserContact
from django.views.generic.detail import DetailView


class ContactForm(DetailView):
    class Meta:
        model = UserContact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
