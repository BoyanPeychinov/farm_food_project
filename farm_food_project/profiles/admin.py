from django.contrib import admin

from farm_food_project.profiles.models import ProducerUserProfile, ConsumerUserProfile


@admin.register(ProducerUserProfile)
class ProducerUserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ConsumerUserProfile)
class ConsumerUserProfileAdmin(admin.ModelAdmin):
    pass
