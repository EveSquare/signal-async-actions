import requests
from celery import shared_task
from django.core.files.base import ContentFile

from sampleblog.models import Blog


@shared_task()
def get_thumbnail(instance_pk):
    print("start get_thumbnail")

    res = requests.get("https://dog.ceo/api/breeds/image/random")

    image_url = res.json()["message"]
    image_res = requests.get(image_url)

    instance = Blog.objects.get(pk=instance_pk)
    instance.thumbnail.save(
        image_url.split("/")[-1],
        ContentFile(image_res.content),
    )
    instance.save()

    print("end get_thumbnail")
