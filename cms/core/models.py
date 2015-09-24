# encoding: utf-8
# -*- coding: utf-8 -*-

from django.db import models
from django import forms

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index

from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailcore.blocks import  StructBlock, ListBlock, \
    StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock


from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from taggit.models import TaggedItemBase

from .fields import ColorField

### Streamfield blocks and config ###

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left','Wrap left'),
        ('right','Wrap right'),
        ('half','Half width'),
        ('full','Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    alignment = ImageFormatChoiceBlock()
    caption = CharBlock()
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"


class PhotoGridBlock(StructBlock):
    images = ListBlock(ImageChooserBlock())

    class Meta:
        icon = "grip"


class PullQuoteBlock(StructBlock):
    quote = CharBlock(classname="quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class PullQuoteImageBlock(StructBlock):
    quote = CharBlock()
    attribution = CharBlock()
    image = ImageChooserBlock(required=False)


class BustoutBlock(StructBlock):
    image = ImageChooserBlock()
    text = RichTextBlock()

    class Meta:
        icon = "pick"


class StatsBlock(StructBlock):
    pass

    class Meta:
        icon = "order"


class StoryBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image")
    bustout = BustoutBlock()
    pullquote = PullQuoteBlock()
    raw_html = RawHTMLBlock(label='Raw HTML', icon="code")
    embed = EmbedBlock(icon="code")
    # photogrid = PhotoGridBlock()
    # testimonial = PullQuoteImageBlock(label="Testimonial", icon="group")
    # stats = StatsBlock()


EVENT_AUDIENCE_CHOICES = (
    ('public', "Public"),
    ('private', "Private"),
)

SHOW_TITLE = ((True, 'Sim'), (False, 'Não'))


# A couple of abstract classes that contain commonly used fields

class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class ContactFields(models.Model):
    telephone_1 = models.CharField(max_length=20, blank=True, verbose_name="Telefone 01")
    telephone_2 = models.CharField(max_length=20, blank=True, verbose_name="Telefone 02")
    telephone_3 = models.CharField(max_length=20, blank=True, verbose_name="Telefone 03")
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True, verbose_name="Endereço")

    panels = [
        FieldPanel('address'),
        FieldPanel('email'),
        FieldPanel('fax'),
        FieldPanel('telephone_1'),
        FieldPanel('telephone_2'),
        FieldPanel('telephone_3'),
    ]

    class Meta:
        abstract = True


# Carousel items

class CarouselItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField("Embed URL", blank=True)
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


# Related links

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


# Advert Snippet

class AdvertPlacement(models.Model):
    page = ParentalKey('wagtailcore.Page', related_name='advert_placements')
    advert = models.ForeignKey('core.Advert', related_name='+')


class Advert(models.Model):
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='adverts',
        null=True,
        blank=True
    )
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        PageChooserPanel('page'),
        FieldPanel('url'),
        FieldPanel('text'),
    ]

    def __unicode__(self):
        return self.text


register_snippet(Advert)


# Home Page

class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('core.HomePage', related_name='carousel_items')


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('core.HomePage', related_name='related_links')


class HomePage(Page):
    body = RichTextField(blank=True)

    streamfield = StreamField(StoryBlock(), null=False)

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    class Meta:
        verbose_name = "Modelo Home Index"


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel('carousel_items', label="Itens de Slide"),
    FieldPanel('body', classname="full"),
    StreamFieldPanel('streamfield'),
    InlinePanel('related_links', label="Links Relecionados"),
]

HomePage.promote_panels = Page.promote_panels


# Product index page

class ProductIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('core.ProductIndexPage', related_name='related_links')


class ProductIndexPage(Page):
    intro = RichTextField(blank=True)

    show_title = models.BooleanField(max_length=3, verbose_name='Mostrar Título da Página', choices=SHOW_TITLE,
                                     default=True)
    title_font_color = ColorField(blank=True, verbose_name="Cor do Título")

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagem do Topo"
    )

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    class Meta:
        verbose_name = "Modelo Produtos Index"


ProductIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('show_title', classname="full title"),
    FieldPanel('title_font_color', classname="full title"),
    ImageChooserPanel('title_image'),
    FieldPanel('intro', classname="full"),
    InlinePanel('related_links', label="Related links"),
]

ProductIndexPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


# Product page

class ProductPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('core.ProductPage', related_name='carousel_items')


class ProductPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('core.ProductPage', related_name='related_links')


class ProductPage(Page):
    intro = RichTextField(blank=True)

    show_title = models.BooleanField(max_length=3, verbose_name='Mostrar Título da Página', choices=SHOW_TITLE,
                                     default=True)
    title_font_color = ColorField(blank=True, verbose_name="Cor do Título")

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagem do Topo"
    )

    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    class Meta:
        verbose_name = "Modelo Produto"


ProductPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('show_title', classname="full title"),
    FieldPanel('title_font_color', classname="full title"),
    ImageChooserPanel('title_image'),
    FieldPanel('intro', classname="full"),
    InlinePanel('carousel_items', label="Carousel items"),
    FieldPanel('body', classname="full"),
    InlinePanel('related_links', label="Related links"),
]

ProductPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


# Work index page

class WorkIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('core.WorkIndexPage', related_name='related_links')


class WorkIndexPage(Page):
    show_title = models.BooleanField(max_length=3, verbose_name='Mostrar Título da Página', choices=SHOW_TITLE,
                                     default=True)
    title_font_color = ColorField(blank=True, verbose_name="Cor do Título")

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagem do Topo"
    )
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    @property
    def Works(self):
        # Get list of live Work pages that are descendants of this page
        Works = WorkPage.objects.live().descendant_of(self)

        # Order by most recent date first
        Works = Works.order_by('-date')

        return Works

    def get_context(self, request):
        # Get Works
        Works = self.Works

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            Works = Works.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(Works, 10)  # Show 10 Works per page
        try:
            Works = paginator.page(page)
        except PageNotAnInteger:
            Works = paginator.page(1)
        except EmptyPage:
            Works = paginator.page(paginator.num_pages)

        # Update template context
        context = super(WorkIndexPage, self).get_context(request)
        context['Works'] = Works
        return context

    class Meta:
        verbose_name = "Modelo Trabalhos Index"


WorkIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('show_title', classname="full title"),
    FieldPanel('title_font_color', classname="full title"),
    ImageChooserPanel('title_image'),
    FieldPanel('intro', classname="full"),
    InlinePanel('related_links', label="Related links"),
]

WorkIndexPage.promote_panels = Page.promote_panels


# Work page

class WorkPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('core.WorkPage', related_name='carousel_items')


class WorkPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('core.WorkPage', related_name='related_links')


class WorkPageTag(TaggedItemBase):
    content_object = ParentalKey('core.WorkPage', related_name='tagged_items')


class WorkPage(Page):
    show_title = models.BooleanField(max_length=3, verbose_name='Mostrar Título da Página', choices=SHOW_TITLE,
                                     default=True)
    title_font_color = ColorField(blank=True, verbose_name="Cor do Título")

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagem do Topo"
    )

    body = RichTextField()
    tags = ClusterTaggableManager(through=WorkPageTag, blank=True)
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    @property
    def Work_index(self):
        # Find closest ancestor which is a Work index
        return self.get_ancestors().type(WorkIndexPage).last()

    class Meta:
        verbose_name = "Modelo Trabalho"


WorkPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('show_title', classname="full title"),
    FieldPanel('title_font_color', classname="full title"),
    ImageChooserPanel('title_image'),
    FieldPanel('date'),
    FieldPanel('body', classname="full"),
    InlinePanel('carousel_items', label="Carousel items"),
    InlinePanel('related_links', label="Related links"),
]

WorkPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
    FieldPanel('tags'),
]


# Contact page

class ContactPage(Page, ContactFields):
    show_title = models.BooleanField(max_length=3, verbose_name='Mostrar Título da Página', choices=SHOW_TITLE,
                                     default=True)
    title_font_color = ColorField(blank=True, verbose_name="Cor do Título")

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagem do Topo"
    )
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    class Meta:
        verbose_name = "Modelo Contatos"


ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('show_title', classname="full title"),
    FieldPanel('title_font_color', classname="full title"),
    ImageChooserPanel('title_image'),
    FieldPanel('body', classname="full"),
    MultiFieldPanel(ContactFields.panels, "Contact"),
]

ContactPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


# Event index page

class CompanyIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('core.CompanyIndexPage', related_name='related_links')


class CompanyIndexPage(Page):
    intro = RichTextField(blank=True, verbose_name='Descrição')

    show_title = models.BooleanField(max_length=3, verbose_name='Mostrar Título da Página', choices=SHOW_TITLE,
                                     default=True)
    title_font_color = ColorField(blank=True, verbose_name="Cor do Título")

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagem do Topo"
    )

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    class Meta:
        verbose_name = "Modelo Empresa"


CompanyIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('show_title', classname="full title"),
    FieldPanel('title_font_color', classname="full title"),
    ImageChooserPanel('title_image'),
    FieldPanel('intro', classname="full"),
    InlinePanel('related_links', label="Links Relacionados"),
]

CompanyIndexPage.promote_panels = Page.promote_panels
