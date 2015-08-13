from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse 
from videos.models import ContentBase
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.TextField(blank = True, null = True)
	city = models.CharField(blank = True, null = True, max_length = 25)
	state = models.CharField(blank = True, null = True, max_length = 25)
	personal_website = models.URLField(blank = True, null = True)
	github_username = models.CharField(blank = True, null = True, max_length = 25)
	phone_number = models.CharField(blank = True, null = True, max_length = 50)
	

	def __unicode__(self):
		return "%s" %(self.user.username)

	def get_absolute_url(self):
		return reverse('user-detail', kwargs={'username' : self.username})




class UserContentItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank = True)
	content = models.ForeignKey(ContentBase, blank = True, null = True, related_name = 'ContentBases')
	content_state = models.CharField(max_length = 23, blank = True, null = True, default = "None")
	active = models.BooleanField(default = True)

	def __unicode__(self):
		return str(self.id)

	def get_content_id(self):
		return self.content.contentbase.id



