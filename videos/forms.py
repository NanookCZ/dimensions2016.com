from django import forms
from .models import Author

class ReccommendContentForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('link', 'comment', 'is_visible', )
		widgets = {
            'link': forms.TextInput(attrs={'placeholder': 'Link'}),
            'comment': forms.Textarea(
                attrs={'placeholder': 'Your comment (not required)'}),
            'is_visible': forms.CheckboxInput(attrs={'value': 'Link'}),
        }
		
