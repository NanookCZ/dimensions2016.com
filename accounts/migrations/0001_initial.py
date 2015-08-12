# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContentItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_state', models.CharField(default='None', max_length=7, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.ForeignKey(related_name='ContentBases', blank=True, to='videos.ContentBase', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('city', models.CharField(max_length=25, null=True, blank=True)),
                ('state', models.CharField(max_length=25, null=True, blank=True)),
                ('personal_website', models.URLField(null=True, blank=True)),
                ('github_username', models.CharField(max_length=25, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
