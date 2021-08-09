from django.db import models

from farm_food_project.profiles.models import ProducerUserProfile


class Product(models.Model):
    MEAT = 'meat'
    MILK = 'milk'
    VEGETABLE = 'vegetable'
    FRUIT = 'fruit'

    CHOICES = (
        (MEAT, 'Meat'),
        (MILK, 'Milk'),
        (VEGETABLE, "Vegetable"),
        (FRUIT, 'Fruit')
    )

    product_type = models.CharField(
        max_length=9,
        choices=CHOICES,
        default=MEAT,
    )

    name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    quantity = models.IntegerField(
       blank=True,
       null=True,
    )

    price = models.FloatField(
        blank=True,
        null=True,
    )

    product_image = models.ImageField(
        upload_to='product',
    )

    producer_profile = models.ForeignKey(
        ProducerUserProfile,
        on_delete=models.CASCADE,
    )