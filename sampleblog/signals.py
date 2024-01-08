from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Blog
from .tasks import get_thumbnail


@receiver(post_save, sender=Blog)
def create_blog(sender, instance, created, **kwargs):
    if created:
        print("Blog created!")
        get_thumbnail.apply_async(
            args=(instance.pk,),
        )
        print("Task sent!")
