from django import template

register = template.Library()

@register.filter
def text(value):
    if isinstance(value, dict):
        return value.get("#text", "")
    return ""