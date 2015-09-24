# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import modelcluster.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0003_add_verbose_names'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0014_auto_20150923_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name=b'External link', blank=True)),
                ('title', models.CharField(help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='EventIndexPage',
            new_name='CompanyIndexPage',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='page',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField([(b'h2', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'h3', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'h4', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'aligned_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'alignment', core.models.ImageFormatChoiceBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock()), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))], label=b'Aligned image')), (b'bustout', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'text', wagtail.wagtailcore.blocks.RichTextBlock())])), (b'pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.CharBlock(classname=b'quote title')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock())])), (b'raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon=b'code', label=b'Raw HTML')), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'code'))]),
        ),
        migrations.DeleteModel(
            name='EventIndexPageRelatedLink',
        ),
        migrations.AddField(
            model_name='companyindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.CompanyIndexPage'),
        ),
    ]
