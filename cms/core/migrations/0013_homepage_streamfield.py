# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import core.models
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150817_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField([(b'h2', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'h3', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'h4', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'aligned_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'alignment', core.models.ImageFormatChoiceBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock()), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))], label=b'Aligned image')), (b'bustout', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'text', wagtail.wagtailcore.blocks.RichTextBlock())])), (b'pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.CharBlock(classname=b'quote title')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock())])), (b'raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon=b'code', label=b'Raw HTML')), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'code'))], null=True),
        ),
    ]
