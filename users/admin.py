from django.contrib import admin
from .models import *
from users.models import User


class ApplicationAdmin(admin.ModelAdmin):
	list_display = ['id','associate','post','associate_is_rated','associate_rating','fellow_is_rated','fellow_rating', 'recall']

admin.site.register(User)
admin.site.register(ProfileFellow)
admin.site.register(ProfileAssociate)
admin.site.register(Application, ApplicationAdmin)
# admin.site.register(Document)
