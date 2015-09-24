# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0002_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wagtailsearch', '0002_add_verbose_names'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('core', '0007_auto_20150814_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagecarouselitem',
            name='page',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='page',
        ),
        migrations.RemoveField(
            model_name='formfield',
            name='page',
        ),
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='EventPage',
        ),
        migrations.DeleteModel(
            name='EventPageCarouselItem',
        ),
        migrations.DeleteModel(
            name='EventPageRelatedLink',
        ),
        migrations.DeleteModel(
            name='EventPageSpeaker',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
