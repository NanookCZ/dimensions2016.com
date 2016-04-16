# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20150813_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentbase',
            name='paid_course',
            field=models.CharField(default='no', max_length=10, null=True, blank=True),
        ),
    ]
