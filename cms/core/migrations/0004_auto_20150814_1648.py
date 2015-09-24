# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import models, migrations

import wagtail.wagtailcore.fields

from core import fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('core', '0003_eventindexpage_title_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventindexpage',
            options={'verbose_name': 'Modelo Empresa'},
        ),
        migrations.AddField(
            model_name='standardindexpage',
            name='show_title',
            field=models.BooleanField(default=True, max_length=3, verbose_name=b'Mostrar T\xc3\xadtulo da P\xc3\xa1gina', choices=[(True, b'Sim'), (False, b'N\xc3\xa3o')]),
        ),
        migrations.AddField(
            model_name='standardindexpage',
            name='title_font_color',
            field=fields.ColorField(verbose_name=b'Cor do T\xc3\xadtulo', blank=True),
        ),
        migrations.AddField(
            model_name='standardindexpage',
            name='title_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='eventindexpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True),
        ),
        migrations.AlterField(
            model_name='eventindexpage',
            name='title_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
