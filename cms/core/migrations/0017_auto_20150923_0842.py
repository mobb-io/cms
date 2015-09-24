# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import core.fields
import modelcluster.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('wagtailredirects', '0002_add_verbose_names'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('wagtaildocs', '0003_add_verbose_names'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('core', '0016_auto_20150923_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('show_title', models.BooleanField(default=True, max_length=3, verbose_name=b'Mostrar T\xc3\xadtulo da P\xc3\xa1gina', choices=[(True, b'Sim'), (False, b'N\xc3\xa3o')])),
                ('title_font_color', core.fields.ColorField(verbose_name=b'Cor do T\xc3\xadtulo', blank=True)),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('title_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'Modelo Produtos Index',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductIndexPageRelatedLink',
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
            name='ProductPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('show_title', models.BooleanField(default=True, max_length=3, verbose_name=b'Mostrar T\xc3\xadtulo da P\xc3\xa1gina', choices=[(True, b'Sim'), (False, b'N\xc3\xa3o')])),
                ('title_font_color', core.fields.ColorField(verbose_name=b'Cor do T\xc3\xadtulo', blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('title_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Imagem do Topo', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'Modelo Produto',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name=b'External link', blank=True)),
                ('embed_url', models.URLField(verbose_name=b'Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('link_document', models.ForeignKey(related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.ProductPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name=b'External link', blank=True)),
                ('title', models.CharField(help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
                ('link_page', models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='core.ProductPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='standardindexpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='standardindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='standardindexpage',
            name='title_image',
        ),
        migrations.RemoveField(
            model_name='standardindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='standardindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='standardindexpagerelatedlink',
            name='page',
        ),
        migrations.RemoveField(
            model_name='standardpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='standardpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='standardpage',
            name='title_image',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='standardpagecarouselitem',
            name='page',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='StandardIndexPage',
        ),
        migrations.DeleteModel(
            name='StandardIndexPageRelatedLink',
        ),
        migrations.DeleteModel(
            name='StandardPage',
        ),
        migrations.DeleteModel(
            name='StandardPageCarouselItem',
        ),
        migrations.DeleteModel(
            name='StandardPageRelatedLink',
        ),
        migrations.AddField(
            model_name='productindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True),
        ),
        migrations.AddField(
            model_name='productindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.ProductIndexPage'),
        ),
    ]
