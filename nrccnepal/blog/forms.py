from django import forms
from .models import UserComments


class CommentForm(forms.ModelForm):
	class Meta:
		model = UserComments
		fields = ['name', 'email', 'message']
		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'comment-name', 'placeholder': "Enter your name"}),
		'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'comment-email', 'placeholder': "Enter your email"}),
		'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'comment-message', 'placeholder': "Enter your response", 'cols': 30, 'rows': 10})
		}
