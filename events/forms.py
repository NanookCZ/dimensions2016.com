from django import forms
from django.core.exceptions import ObjectDoesNotExist
from .models import Guest, Event
from django.utils.text import slugify
import itertools
from bootstrap3_datetime.widgets import DateTimePicker


ATTENDING_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    )


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('attending_status', 'comment')
        widgets = {
        'comment': forms.TextInput(attrs={'placeholder': 'Add your comment here'}),
        }


class EventForm(forms.ModelForm):
    event_start = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    event_end = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    time_of_event = forms.DateField(
        widget=DateTimePicker(options={"format": "HH:mm:ss",
                                       "pickDate": False}))
    class Meta:
        model = Event
        fields = ('title', 'description', 'event_start', 'event_end', 'time_of_event', 'street_address', 'city', 'state', 'zip_code', 'telephone', 'category')
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Add event title'}),
        'description': forms.Textarea(attrs={'placeholder': 'Add event description'}),
        'event_start': forms.TextInput(attrs={'placeholder': 'Add event start date'}),
        'event_end': forms.TextInput(attrs={'placeholder': 'Add event end date'}),
        'telephone': forms.TextInput(attrs={'placeholder': 'Organiser phone number'}),
        'time_of_event': forms.TextInput(attrs={'placeholder': 'Event start time'}),
        'street_address': forms.TextInput(attrs={'placeholder': 'Event street address'}),
        'city': forms.TextInput(attrs={'placeholder': 'Event city'}),
        'state': forms.TextInput(attrs={'placeholder': 'Event state'}),
        'zip_code': forms.TextInput(attrs={'placeholder': 'Event city zip code'}),
        }
    
    def save(self):
        instance = super(EventForm, self).save(commit=False)
        instance.slug = orig = slugify(instance.title)
        for x in itertools.count(1):
            if not Event.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
        instance.save()
        return instance
        
    