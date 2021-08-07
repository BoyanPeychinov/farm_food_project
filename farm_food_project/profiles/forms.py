from django import forms

from farm_food_project.profiles.models import ProducerUserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProducerUserProfile
        exclude = ('user',)
