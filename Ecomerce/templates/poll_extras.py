from django import template
register = template.Library()

@register.simple_tag()
def multiply(product,cart):
    return product.price * quantity(product,cart)