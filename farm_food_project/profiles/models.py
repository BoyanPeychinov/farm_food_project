from django.db import models

from ..farm_food_auth.models import FarmFoodUser


class ProducerUserProfile(models.Model):
    name = models.CharField(
        max_length=50,
    )

    description = models.TextField()

    location = models.CharField(
        max_length=100,
    )

    phone_number = models.IntegerField(
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    # products = None

    user = models.OneToOneField(
        FarmFoodUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name


class ConsumerUserProfile(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    phone_number = models.IntegerField(
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    user = models.OneToOneField(
        FarmFoodUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from .signals import *