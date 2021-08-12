import os
from os.path import join

from django import forms
from django.conf import settings

from farm_food_project.profiles.models import ProducerUserProfile, ConsumerUserProfile


class ProducerProfileForm(forms.ModelForm):
    class Meta:
        model = ProducerUserProfile
        exclude = ('user',)


class EditProducerProfileForm(ProducerProfileForm):
    class Meta:
        model = ProducerUserProfile
        exclude = ('user',)

    def save(self, commit=True):
        db_producer = ProducerUserProfile.objects.get(pk=self.instance.user_id)
        if commit and db_producer.profile_image:
            os.remove(join(settings.MEDIA_ROOT, str(db_producer.profile_image)))
        return super().save(commit)


class ConsumerProfileForm(forms.ModelForm):
    class Meta:
        model = ConsumerUserProfile
        exclude = ('user',)


class EditConsumerProfileForm(ConsumerProfileForm):
    class Meta:
        model = ConsumerUserProfile
        exclude = ('user',)

    def save(self, commit=True):
        db_consumer = ConsumerUserProfile.objects.get(pk=self.instance.user_id)
        if commit and db_consumer.profile_image:
            os.remove(join(settings.MEDIA_ROOT, str(db_consumer.profile_image)))
        return super().save(commit)
