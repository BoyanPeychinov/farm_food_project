from django.urls import reverse

from farm_food_project.product.models import Product
from farm_food_project.profiles.models import ProducerUserProfile
from tests.base.tests import ProducerProfileTestCase


class TestProductDetailsView(ProducerProfileTestCase):
    def test__getProductDetails_withoutLoggedUser_shouldRedirectToLoginView(self):
        profile = ProducerUserProfile.objects.get(user_id=self.user.id)
        profile.name = 'Boyan'
        Product.objects.create(
            product_type=Product.MILK,
            name='test_name',
            quantity='5',
            price='10',
            product_image='path/to/image.png',
            producer_profile=profile
        )
        profile.save()

        response = self.client.get(reverse('product details', kwargs={'pk': profile.pk}))

        self.assertEqual(302, response.status_code)

    def test__getProductDetails_withLoggedUser_shouldRedirectToProductDetails(self):
        self.client.force_login(self.user)
        profile = ProducerUserProfile.objects.get(user_id=self.user.id)
        profile.name = 'Boyan'
        product = Product.objects.create(
            product_type=Product.MILK,
            name='test_name',
            quantity='5',
            price='10',
            product_image='path/to/image.png',
            producer_profile=profile
        )
        profile.save()

        response = self.client.get(reverse('product details', kwargs={'pk': profile.pk}))

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['product'], product)
        self.assertTrue(response.context['is_owner'])