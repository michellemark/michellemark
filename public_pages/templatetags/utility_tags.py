from django import template

register = template.Library()


@register.simple_tag
def make_list(*args):

    return args
