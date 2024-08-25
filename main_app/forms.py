from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['note']
        # widgets = {
        #     'date': forms.DateInput(
        #         format=('%Y-%m-%d'),
        #         attrs={
        #             'placeholder': 'Select a date',
        #             'type': 'date'
        #         }
        #     ),
        # }