import os
from os.path import join

import random
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from farm_food_project.product.models import Product
from farm_food_project.profiles.models import ProducerUserProfile
from tests.base.tests import ProducerProfileTestCase


class TestCreateProductView(ProducerProfileTestCase):
    def test__createProductWithoutPriceAndQuantity__shouldNotCreateProduct(self):
        profile = ProducerUserProfile.objects.get(user_id=self.user.id)
        profile.name = 'Boyan'
        product_to_create = {
            'product_type': 'milk',
            'name': 'test_name',
            'product_image': 'path/to/image.png',
        }
        self.client.force_login(self.user)

        response = self.client.post(reverse('create product'), data=product_to_create)

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(Product.objects.all()))


    def test__createProductWithRightData__shouldCreateProduct(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'dog.jpg')
        file_name = f"{random.randint(1, 100000)}-dog.jpg"
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpg',
        )

        profile = ProducerUserProfile.objects.get(user_id=self.user.id)
        profile.name = 'Boyan'
        product_to_create = {
            'product_type': Product.MILK,
            'name': 'test_name',
            'quantity': 5,
            'price': 10,
            'product_image': file,
        }
        self.client.force_login(self.user)

        response = self.client.post(reverse('create product'), data=product_to_create)

        self.assertEqual(302, response.status_code)
        self.assertEqual(1, len(Product.objects.all()))

        product = Product.objects.get(producer_profile_id=profile.id)
        os.remove(join(settings.MEDIA_ROOT, str(product.product_image)))
