# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20150923_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagecarouselitem',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='homepagecarouselitem',
            name='embed_url',
        ),
        migrations.RemoveField(
            model_name='productpagecarouselitem',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='productpagecarouselitem',
            name='embed_url',
        ),
        migrations.RemoveField(
            model_name='workpagecarouselitem',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='workpagecarouselitem',
            name='embed_url',
        ),
    ]
