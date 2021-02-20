from django.contrib import admin
from .models import *
from users.models import User


class ApplicationAdmin(admin.ModelAdmin):
	list_display = ['id','associate','post','sent_to_employer','rejected','is_hired','associate_complained','associates_complaint_updating','associates_complaint_resolved','fellow_complained','fellows_complaint_resolved','fellows_complaint_updating','associate_is_rated','fellow_is_rated','recall']

admin.site.register(User)
admin.site.register(ProfileFellow)
admin.site.register(ProfileAssociate)
admin.site.register(Application, ApplicationAdmin)
# admin.site.register(Document)
