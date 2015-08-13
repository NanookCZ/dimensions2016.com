# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20150812_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentbase',
            name='slug',
            field=models.SlugField(unique=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='contentbase',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
