from django.contrib import admin
from .models import *
from users.models import User

admin.site.register(User)
admin.site.register(ProfileFellow)
admin.site.register(ProfileAssociate)
admin.site.register(Application)
# admin.site.register(Document)
