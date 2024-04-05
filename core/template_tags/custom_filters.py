
from django import template

register = template.Library()

# AÑADIR CLASES DE BOOTSTRAP

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})
