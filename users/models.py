from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/", null=True, blank=True, verbose_name="Аватар"
    )
    phone_number = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Номер телефона"
    )
    country = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Страна"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
