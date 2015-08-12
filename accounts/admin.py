from django.contrib import admin
from .models import UserContentItem, UserProfile

admin.site.register(UserProfile)
admin.site.register(UserContentItem)