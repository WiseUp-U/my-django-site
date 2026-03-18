from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        from .createsuperuser import create_superuser
        create_superuser()
