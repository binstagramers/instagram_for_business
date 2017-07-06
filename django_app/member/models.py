from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image_profile = models.ImageField(blank=True)
