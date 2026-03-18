from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        from .createsuperuser import create_superuser
        post_migrate.connect(create_superuser, sender=self)
