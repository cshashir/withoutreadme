from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ['id','job_title','is_verified','is_rejected','start_date','end_date','vacancy','no_of_hirings','filled']



class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['id','subject','contacted','resolved']



admin.site.register(Post, PostAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
