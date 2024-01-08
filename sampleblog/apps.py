from django.apps import AppConfig
from django.core.signals import request_finished


class SampleblogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sampleblog"

    def ready(self):
        from .signals import create_blog

        request_finished.connect(create_blog, sender=self)
