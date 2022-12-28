from django import template

register = template.Library()

"""
Возвращает verbose_name для поля.
"""


@register.simple_tag
def get_verbose_field_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name
