from django.db import models
from django.contrib.auth.models import AbstractUser

from realtimechat.helpers import create_hash


class User(AbstractUser):
    hash_id = models.CharField(
        max_length=32, default=create_hash, unique=True)