# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('slug', models.SlugField(unique=True, max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ContentBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('free_preview', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=True)),
                ('embed_code', models.CharField(max_length=500, null=True, blank=True)),
                ('embed_code_bigger', models.CharField(max_length=500, null=True, blank=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True)),
                ('is_bigger', models.BooleanField(default=False)),
                ('share_link', models.URLField(max_length=100, null=True, blank=True)),
                ('share_message', models.TextField(default='Checkout this awesome video.  ', null=True, blank=True)),
                ('related_image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True)),
                ('approved_by_admin', models.BooleanField(default=True)),
                ('month_course', models.CharField(default='no', max_length=10, null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, to='videos.Category', null=True)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('image', models.ImageField(null=True, upload_to='images/', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='Unknown', max_length=100, null=True, blank=True)),
                ('source_link', models.URLField(max_length=100, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Sourcies',
            },
        ),
        migrations.AddField(
            model_name='contentbase',
            name='content_type',
            field=models.ForeignKey(blank=True, to='videos.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='contentbase',
            name='reccommend_by',
            field=models.ForeignKey(blank=True, to='videos.Author', null=True),
        ),
        migrations.AddField(
            model_name='contentbase',
            name='source',
            field=models.ForeignKey(blank=True, to='videos.Source', null=True),
        ),
    ]
