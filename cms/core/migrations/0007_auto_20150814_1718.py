# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from core import fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('core', '0006_auto_20150814_1714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'Modelo Trabalhos Index'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'Modelo Trabalho'},
        ),
        migrations.AddField(
            model_name='blogpage',
            name='show_title',
            field=models.BooleanField(default=True, max_length=3, verbose_name=b'Mostrar T\xc3\xadtulo da P\xc3\xa1gina', choices=[(True, b'Sim'), (False, b'N\xc3\xa3o')]),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='title_font_color',
            field=fields.ColorField(verbose_name=b'Cor do T\xc3\xadtulo', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='title_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
