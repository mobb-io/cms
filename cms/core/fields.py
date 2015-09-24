from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db.models import CharField

from core import forms, widgets


class ColorField(CharField):
    """Field for database models"""
    widget = widgets.ColorFieldWidget
    default_validators = [RegexValidator(regex=forms.RGB_REGEX)]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs.update({
            'form_class': forms.RGBColorField,
            'widget': self.widget,
        })
        return super(ColorField, self).formfield(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ColorField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs