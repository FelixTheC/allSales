from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='get_first_collar_type')
def get_first_collar_type(value):
    for _ in value:
        try:
            return _.producttype.name
        except AttributeError:
            return 0