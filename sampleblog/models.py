from django.db import models

from config import settings


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    thumbnail = models.ImageField(
        upload_to="blog/thumbnails",
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title
