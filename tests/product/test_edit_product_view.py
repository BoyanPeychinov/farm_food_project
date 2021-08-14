import os
from os.path import join
import random

from django.conf import settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from farm_food_project.product.models import Product
from farm_food_project.profiles.models import ProducerUserProfile
from tests.base.tests import ProducerProfileTestCase


class TestEditProductView(ProducerProfileTestCase):
    def test_postDetailsWithRightData_shouldAddData(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'dog.jpg')
        file_name = f"{random.randint(1, 100000)}-dog.jpg"
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpg',
        )

        profile = ProducerUserProfile.objects.get(user_id=self.user.id)
        profile.name = 'Boyan'
        product = Product.objects.create(
            product_type= Product.MEAT,
            name='name',
            quantity=2,
            price=20,
            product_image='path/to/image.png',
            producer_profile=profile
        )

        data_for_edit = {
            'name': 'test_name',
            'quantity': 5,
            'price': 10,
            'product_image': file,
        }
        self.client.force_login(self.user)

        response = self.client.post(reverse('edit product', kwargs={'pk': product.id}), data=data_for_edit)

        product = Product.objects.get(producer_profile_id=profile.pk)

        self.assertTrue(str(product.product_image).endswith(file_name))

        os.remove(join(settings.MEDIA_ROOT, str(product.product_image)))

    def test_postDetails_whenUserLoggedInWithImage_shouldChangeImage(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'dog.jpg')
        file_name = f"{random.randint(1, 100000)}-dog.jpg"
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpg',
        )

        profile = ProducerUserProfile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('producer details'), data={
            'name': 'Gosho',
            'description': 'test_description',
            'location': 'test_location',
            'phone_number': 123123123,
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = ProducerUserProfile.objects.get(pk=self.user.id)

        self.assertTrue(str(profile.profile_image).endswith(file_name))

        os.remove(join(settings.MEDIA_ROOT, str(profile.profile_image)))
