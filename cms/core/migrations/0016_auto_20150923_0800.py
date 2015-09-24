# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import core.fields
import modelcluster.fields
import django.db.models.deletion
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0002_add_verbose_names'),
        ('wagtaildocs', '0003_add_verbose_names'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('wagtailimages', '0008_image_created_at_index'),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('core', '0015_auto_20150923_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('show_title', models.BooleanField(default=True, max_length=3, verbose_name=b'Mostrar T\xc3\xadtulo da P\xc3\xa1gina', choices=[(True, b'Sim'), (False, b'N\xc3\xa3o')])),
                ('title_font_color', core.fields.ColorField(verbose_name=b'Cor do T\xc3\xadtulo', blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('title_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'Modelo Trabalhos Index',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WorkIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name=b'External link', blank=True)),
                ('title', models.CharField(help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('show_title', models.BooleanField(default=True, max_length=3, verbose_name=b'Mostrar T\xc3\xadtulo da P\xc3\xa1gina', choices=[(True, b'Sim'), (False, b'N\xc3\xa3o')])),
                ('title_font_color', core.fields.ColorField(verbose_name=b'Cor do T\xc3\xadtulo', blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('date', models.DateField(verbose_name=b'Post date')),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'Modelo Trabalho',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WorkPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name=b'External link', blank=True)),
                ('embed_url', models.URLField(verbose_name=b'Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('link_document', models.ForeignKey(related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.WorkPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name=b'External link', blank=True)),
                ('title', models.CharField(help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='core.WorkPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkPageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='core.WorkPage')),
                ('tag', models.ForeignKey(related_name='core_workpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='title_image',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='title_image',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.DeleteModel(
            name='BlogIndexPage',
        ),
        migrations.DeleteModel(
            name='BlogIndexPageRelatedLink',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.DeleteModel(
            name='BlogPageCarouselItem',
        ),
        migrations.DeleteModel(
            name='BlogPageRelatedLink',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.AddField(
            model_name='workpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='core.WorkPageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='workpage',
            name='title_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='workindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True),
        ),
        migrations.AddField(
            model_name='workindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.WorkIndexPage'),
        ),
    ]
