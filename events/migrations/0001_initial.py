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
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('event_start', models.DateField(null=True, blank=True)),
                ('event_end', models.DateField(null=True, blank=True)),
                ('time_of_event', models.CharField(max_length=50, null=True, blank=True)),
                ('street_address', models.CharField(default='', max_length=255, blank=True)),
                ('city', models.CharField(default='', max_length=64, blank=True)),
                ('state', models.CharField(default='', max_length=64, blank=True)),
                ('zip_code', models.CharField(default='', max_length=10, blank=True)),
                ('telephone', models.CharField(default='', max_length=20, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('month_event', models.CharField(default='no', max_length=10, null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, to='videos.Category', null=True)),
                ('hosted_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attending_status', models.CharField(default='yes', max_length=32, choices=[('yes', 'Yes'), ('no', 'No'), ('maybe', 'Maybe')])),
                ('comment', models.CharField(default='', max_length=255, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(related_name='guests', to='events.Event')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([('event', 'user')]),
        ),
    ]
