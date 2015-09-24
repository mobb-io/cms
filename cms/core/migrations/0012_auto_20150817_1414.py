# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150816_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpagetag',
            name='tag',
            field=models.ForeignKey(related_name='core_blogpagetag_items', to='taggit.Tag'),
        ),
    ]
