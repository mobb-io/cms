# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150814_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='address',
            field=models.CharField(max_length=255, verbose_name=b'Endere\xc3\xa7o', blank=True),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='telephone_1',
            field=models.CharField(max_length=20, verbose_name=b'Telefone 01', blank=True),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='telephone_2',
            field=models.CharField(max_length=20, verbose_name=b'Telefone 02', blank=True),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='telephone_3',
            field=models.CharField(max_length=20, verbose_name=b'Telefone 03', blank=True),
        ),
    ]
