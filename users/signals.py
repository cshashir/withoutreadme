from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_fellow:
            ProfileFellow.objects.create(fellow=instance)
        else:
            ProfileAssociate.objects.create(associate=instance)
    else:
        if instance.is_fellow:
            instance.profilefellow.save()
        else:
            instance.profileassociate.save()
