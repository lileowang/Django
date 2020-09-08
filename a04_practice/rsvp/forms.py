from django import forms


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
    feedback = forms.CharField(widget=forms.Textarea(
        attrs={
            'style': 'width:100%; border: 4px dashed blue;',
            'placeholder': 'your messages'
        }))
