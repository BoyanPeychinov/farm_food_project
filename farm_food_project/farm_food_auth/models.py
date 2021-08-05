from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from farm_food_project.farm_food_auth.managers import FarmFoodUserManager


class FarmFoodUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_producer = models.BooleanField(
        default=False,
    )
    is_consumer = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = FarmFoodUserManager()
