from django.urls import reverse

from farm_food_project.product.models import Product
from farm_food_project.profiles.models import ProducerUserProfile
from tests.base.tests import ProducerProfileTestCase


class TestProducerDetailsView(ProducerProfileTestCase):
    def test__getProducerDetails_withoutLoggedUser_shouldRedirectToLoginView(self):

        response = self.client.get(reverse('producer details'))

        self.assertEqual(302, response.status_code)

    def test__getProducerDetails_withLoggedUser_shouldRedirectToProducerDetailsAndShowProducts(self):
        self.client.force_login(self.user)
        profile = ProducerUserProfile.objects.get(user_id=self.user.id)
        profile.name = 'Boyan'
        Product.objects.create(
            product_type=Product.MILK,
            name='hrana',
            quantity='5',
            price='10',
            product_image='path/to/image.png',
            producer_profile=profile
        )
        profile.save()

        response = self.client.get(reverse('producer details'))

        self.assertEqual(200, response.status_code)
        self.assertListEqual(list(response.context['products']), list(profile.product_set.all()))