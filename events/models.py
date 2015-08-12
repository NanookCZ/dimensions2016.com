from __future__ import unicode_literals
import datetime
from django.core.urlresolvers import reverse 
from django.db import models
from django.db.models import permalink
from django.core.mail import send_mass_mail
from django.template import loader, Context
from django.conf import settings
from django.contrib.sites.models import Site 
from django.contrib.auth.models import User
from videos.models import Category
from events.slug import unique_slugify
from cloudinary.models import CloudinaryField



ATTENDING_CHOICES = (
		('yes', 'Yes'),
		('no', 'No'),
		('maybe', 'Maybe'),
	)

class Event(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique = True)
	description = models.TextField(blank = True, null = True)
	event_start = models.DateField(blank = True, null = True)
	event_end = models.DateField(blank = True, null = True)
	time_of_event = models.CharField(max_length = 50, blank = True, null = True)
	hosted_by = models.ForeignKey(User, blank = True, null = True)
	street_address = models.CharField(max_length=255, blank=True, default='')
	city = models.CharField(max_length=64, blank=True, default='')
	state = models.CharField(max_length=64, blank=True, default='')
	zip_code = models.CharField(max_length=10, blank=True, default='')
	telephone = models.CharField(max_length=20, blank=True, default='')
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	category = models.ForeignKey(Category, blank = True, null = True)
	month_event = models.CharField(max_length = 10, blank = True, null = True, default='no')

	def __unicode__(self):
		return "%s" %(self.title)

	def get_event_address(self):
		return u"%s, %s, %s" %(self.state, self.city, self.street_address)

	def get_absolute_url(self):
		return reverse('event-detail', kwargs={"slug" : self.slug})

	def get_event_id(self):
		return self.id

	def guests_attending(self):
		return self.guests.filter(attending_status='yes')

	def guests_not_attending(self):
		return self.guests.filter(attending_status='no')

	def guests_may_attend(self):
		return self.guests.filter(attending_status='maybe')

	def save(self, **kwargs):
		slug = '%s' % (self.title)
		unique_slugify(self, slug)
		super(Event, self).save()

	

class Guest(models.Model):
    event = models.ForeignKey(Event, related_name='guests')
    user = models.ForeignKey(User, blank = True, null = True)
    attending_status = models.CharField(max_length=32, choices=ATTENDING_CHOICES, default='yes')
    comment = models.CharField(max_length=255, blank=True, default='')
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return u"%s - %s" % (self.event.title, self.attending_status)

    
    class Meta:
        unique_together = ('event', 'user')
