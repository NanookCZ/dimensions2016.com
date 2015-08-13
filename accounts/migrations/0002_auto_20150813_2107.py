# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontentitem',
            name='content_state',
            field=models.CharField(default='None', max_length=23, null=True, blank=True),
        ),
    ]
