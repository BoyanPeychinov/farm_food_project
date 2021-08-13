import os
from os.path import join
import random

from django.conf import settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from farm_food_project.profiles.models import ConsumerUserProfile
from tests.base.tests import ConsumerProfileTestCase


class TestConsumerDetailsView(ConsumerProfileTestCase):
    def test_postDetails_whenUserLoggedInWithoutImage_shouldChangeImage(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'dog.jpg')

        file_name = f"{random.randint(1, 100000)}-dog.jpg"
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpg',
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('consumer detail'), data={
            'name': 'Gosho',
            'phone_number': 123123123,
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = ConsumerUserProfile.objects.get(pk=self.user.id)

        self.assertTrue(str(profile.profile_image).endswith(file_name))

        os.remove(join(settings.MEDIA_ROOT, str(profile.profile_image)))

    def test_postDetails_whenUserLoggedInWithImage_shouldChangeImage(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'dog.jpg')
        file_name = f"{random.randint(1, 100000)}-dog.jpg"
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpg',
        )

        profile = ConsumerUserProfile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('consumer detail'), data={
            'name': 'Gosho',
            'phone_number': 123123123,
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = ConsumerUserProfile.objects.get(pk=self.user.id)

        self.assertTrue(str(profile.profile_image).endswith(file_name))

        os.remove(join(settings.MEDIA_ROOT, str(profile.profile_image)))
