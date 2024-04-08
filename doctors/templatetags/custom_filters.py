
from django import template

register = template.Library()

# AÑADIR CLASES DE BOOTSTRAP

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})
#@register.filter(name='add_class_and_placeholder')
#def add_class_and_placeholder(value, css_class, placeholder_text):
 #   widget_attrs = {'class': css_class, 'placeholder': placeholder_text}
  #  return value.as_widget(attrs=widget_attrs)