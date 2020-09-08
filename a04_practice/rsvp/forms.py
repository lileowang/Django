from django import forms
from django.core.exceptions import ValidationError
import datetime


class RsvpForm(forms.Form):
    name = forms.CharField(
        max_length=10,
        label='your name',
        widget=forms.TextInput(
            attrs={
                'style': 'width:30%; border: 2px dashed red;: red;',
                'placeholder': 'full name',
            }))
    email = forms.EmailField(
        max_length=20,
        label='your email',
        widget=forms.TextInput(
            attrs={
                'style': 'width:30%; border: 3px dashed green;',
                'placeholder': 'valid email',
            }))
    arrival_date = forms.DateField(
        help_text='within next 3 days',
        widget=forms.DateInput(attrs={'type': 'date'}))
    feedback = forms.CharField(widget=forms.Textarea(
        attrs={
            'style': 'width:100%; border: 4px dashed blue;',
            'placeholder': 'your messages'
        }))

    def clean_arrival_date(self):
        data = self.cleaned_data['arrival_date']

        # check if in the past
        if data < datetime.date.today():
            raise ValidationError('cannot be in the past')

        if data > datetime.date.today() + datetime.timedelta(days=3):
            raise ValidationError('cannot be more than 3 days ahead')

        return data
