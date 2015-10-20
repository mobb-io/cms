from datetime import date
from django import template
from django.conf import settings

from ..models import WorkPage, Advert, Page

register = template.Library()


# settings value
@register.assignment_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")




@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('core/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    root = get_site_root(context)
    try:
        is_root_page = (root.id == calling_page.id)
    except:
        is_root_page = False

    menuitems = parent.get_children().filter(
        live=True,
        show_in_menus=True
    ).order_by('title')

    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'is_root_page':is_root_page,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('core/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent, sub=False, level=0):
    menuitems_children = parent.get_children().order_by('title')

    menuitems_children = menuitems_children.live().in_menu()

    for menuitem in menuitems_children:
        menuitem.show_dropdown = has_menu_children(menuitem)

    levelstr= "".join('a' for i in range(level)) # for indentation
    level += 1

    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        'sub': sub,
        'level':level,
        'levelstr':levelstr,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves all live pages which are children of the calling page
#for product index listing
@register.inclusion_tag(
    'core/tags/product_index_listing.html',
    takes_context=True
)
def product_index_listing(context, calling_page):
    pages = calling_page.get_children().live()
    return {
        'pages': pages,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# Work feed for home page
@register.inclusion_tag(
    'core/tags/work_listing_homepage.html',
    takes_context=True
)
def work_listing_homepage(context, count=2):
    works = WorkPage.objects.live().order_by('-date')
    return {
        'works': works[:count].select_related('feed_image'),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# Advert snippets
@register.inclusion_tag('core/tags/adverts.html', takes_context=True)
def adverts(context):
    return {
        'adverts': Advert.objects.select_related('page'),
        'request': context['request'],
    }


@register.inclusion_tag('core/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }
