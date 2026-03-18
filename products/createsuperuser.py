from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

def create_superuser(sender, **kwargs):
    username =settings.DJANGO_SUPERUSER_USERNAME
    email = settings.DJANGO_SUPERUSER_EMAIL
    password = settings.DJANGO_SUPERUSER_PASSWORD
    
    if not username or not password:
        return

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )