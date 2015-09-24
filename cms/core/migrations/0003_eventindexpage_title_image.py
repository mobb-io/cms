# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('core', '0002_auto_20150814_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventindexpage',
            name='title_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
