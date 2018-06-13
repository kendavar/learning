from django import template

register = template.Library()

@register.filter("cut",cut)
def cut(value,arg):
    return value.replace(arg,"")
