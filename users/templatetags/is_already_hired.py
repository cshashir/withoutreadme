from django import template

from users.models import Application

register = template.Library()


@register.simple_tag(name='is_already_hired')
def is_already_hired(post, associate):
	try:
		application = Application.objects.get(post=post, associate=associate)
		if application.is_hired:
			return True
		else:
			return False
	except Application.DoesNotExist:
		return False
