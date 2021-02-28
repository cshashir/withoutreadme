from django import template

from users.models import Application

register = template.Library()


@register.simple_tag(name='is_already_rejected')
def is_already_hired(post, associate):
	try:
		application = Application.objects.get(post=post, associate=associate)
		if application.rejected:
			return True
		else:
			return False
	except Application.DoesNotExist:
		return False
