from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from farm_food_project.profiles.models import ProducerUserProfile, ConsumerUserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created and instance.is_producer:
        profile = ProducerUserProfile(
            user=instance,
        )

        profile.save()
    elif created and instance.is_consumer:
        profile = ConsumerUserProfile(
            user=instance,
        )

        profile.save()