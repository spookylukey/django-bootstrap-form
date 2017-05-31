from django.template.loader import get_template
from django import template

register = template.Library()

@register.filter
def bootstrap(element):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("bootstrapform/field.html")
        context = {'field': element}
    else:
        template = get_template("bootstrapform/form.html")
        context = {'form': element}

    return template.render(context)

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"
