from django import template

from users.models import Application

register = template.Library()


@register.simple_tag(name='is_already_applied')
def is_already_applied(post, associate):
    applied = Application.objects.filter(post=post, associate=associate)
    if applied:
        return True
    else:
        return False
