from .models import UserProfile
from django import forms
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('description', 'city', 'state', 'personal_website', 'github_username', 'phone_number')
		widgets = {
            'desription': forms.Textarea(
                attrs={'placeholder': 'Something about you (not required)'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'personal_website': forms.TextInput(attrs={'placeholder': 'Your personal website'}),
            'github_username': forms.TextInput(attrs={'placeholder': 'Your github username'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Your phone number'}),
        }

class UserBasicForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', )
		widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }
