# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150814_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Modelo Home Index'},
        ),
        migrations.RenameField(
            model_name='contactpage',
            old_name='address_1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='contactpage',
            old_name='telephone',
            new_name='fax',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='city',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='country',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='post_code',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='telephone_1',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='telephone_2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='telephone_3',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
