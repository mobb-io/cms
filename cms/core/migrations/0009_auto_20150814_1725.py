# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from core import fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0002_add_verbose_names'),
        ('wagtailredirects', '0002_add_verbose_names'),
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailsearch', '0002_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('core', '0008_auto_20150814_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='page',
        ),
        migrations.AlterModelOptions(
            name='contactpage',
            options={'verbose_name': 'Modelo Contatos'},
        ),
        migrations.AddField(
            model_name='contactpage',
            name='show_title',
            field=models.BooleanField(default=True, max_length=3, verbose_name=b'Mostrar T\xc3\xadtulo da P\xc3\xa1gina', choices=[(True, b'Sim'), (False, b'N\xc3\xa3o')]),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='title_font_color',
            field=fields.ColorField(verbose_name=b'Cor do T\xc3\xadtulo', blank=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='title_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.DeleteModel(
            name='PersonPage',
        ),
        migrations.DeleteModel(
            name='PersonPageRelatedLink',
        ),
    ]
