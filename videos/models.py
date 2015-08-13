from __future__ import unicode_literals
import urllib2
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse 
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField


class ContentBaseQueryset(models.query.QuerySet):
	def active(self):
		return self.filter(active = True)

	def featured(self):
		return self.filter(featured = True)

class ContentBaseManager(models.Manager):
	def get_queryset(self):
		return ContentBaseQueryset(self.model, using=self._db)

	def get_featured(self):
		return self.get_queryset().active().featured().order_by('created_date')

DEFAULT_MESSAGE = "Checkout this awesome video.  "
class ContentBase(models.Model):
	title = models.CharField(max_length = 150)
	slug = models.SlugField(max_length = 150, unique = True)
	description = models.TextField()
	category = models.ForeignKey("Category", null = True, blank = True)
	content_type = models.ForeignKey("ContentType", null = True, blank = True)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	active = models.BooleanField(default = True)
	free_preview = models.BooleanField(default = True)
	featured = models.BooleanField(default = True)
	embed_code = models.CharField(max_length = 500, blank = True, null = True)
	embed_code_bigger = models.CharField(max_length = 500, blank = True, null = True)
	image = CloudinaryField('image', blank = True, null = True)
	is_bigger = models.BooleanField(default = False)
	source = models.ForeignKey("Source", blank = True, null = True)
	share_link = models.URLField(max_length = 100, blank = True, null = True)
	share_message = models.TextField(blank = True, null = True, default = DEFAULT_MESSAGE)
	reccommend_by = models.ForeignKey("Author", blank = True, null = True)
	related_image = CloudinaryField('image', blank = True, null = True)
	approved_by_admin = models.BooleanField(default = True)
	objects = ContentBaseManager()
	month_course = models.CharField(max_length = 10, blank = True, null = True, default='no')

	def __unicode__(self):
		return "%s" %(self.title)

	def get_title(self):
		return str(self.title)

	def get_slug(self):
		return str(self.slug)

	def get_absolute_url(self):
		return reverse('content-detail', kwargs={"slug_con" : self.slug})

	def get_content_type(self):
		return str(self.content_type.id)

	def get_content_id(self):
		return str(self.id)

	def get_share_link(self):
		full_url = "%s%s" %(settings.FULL_DOMAIN_NAME, self.get_absolute_url())
		return full_url

	def get_share_message(self):
		full_url = "%s%s" %(settings.FULL_DOMAIN_NAME, self.get_absolute_url())
		return urllib2.Request(self.share_message,  full_url)

	class Meta:
		ordering = ['created_date']


class Source(models.Model):
	title = models.CharField(max_length = 100, blank = True, null = True)
	source_link = models.URLField(max_length = 100, blank = True, null = True)
	active = models.BooleanField(default = True)

	class Meta:
		verbose_name_plural = 'Sourcies'

	def __unicode__(self):
		return "%s" %(self.title)

class Author(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, blank = True, null = True)
	is_visible = models.BooleanField(default = True)
	active = models.BooleanField(default = True)
	link = models.URLField(blank = True, null = True)
	comment = models.TextField(blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.author.username)


class Category(models.Model):
	title = models.CharField(max_length = 25)
	slug = models.SlugField(max_length = 25, unique = True)
	active = models.BooleanField(default = True)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s" %(self.title)

	def get_absolute_url(self):
		return reverse('category', kwargs={"slug_cat" : self.slug})

	class Meta:
		verbose_name_plural = 'Categories'

class ContentType(models.Model):
	title = models.CharField(max_length = 20)
	slug = models.SlugField(max_length = 20, unique = True)
	image = CloudinaryField('image', blank = True, null = True)
	active = models.BooleanField(default = True)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s" %(self.title)

	def get_absolute_url(self):
		return reverse('content-type', kwargs={"slug" : self.slug})














