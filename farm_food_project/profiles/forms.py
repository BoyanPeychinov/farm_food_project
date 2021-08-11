import os
from os.path import join

from django import forms
from django.conf import settings

from farm_food_project.profiles.models import ProducerUserProfile, ConsumerUserProfile


class ProducerProfileForm(forms.ModelForm):
    class Meta:
        model = ProducerUserProfile
        exclude = ('user',)

    def save(self, commit=True):
        db_producer = ProducerUserProfile.objects.get(pk=self.instance.id)
        if commit:
            os.remove(join(settings.MEDIA_ROOT, str(db_producer.profile_image)))
        return super().save(commit)


class ConsumerProfileForm(forms.ModelForm):
    class Meta:
        model = ConsumerUserProfile
        exclude = ('user',)
