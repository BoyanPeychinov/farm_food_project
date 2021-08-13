from django.urls import reverse

from farm_food_project.profiles.models import ConsumerUserProfile
from tests.base.tests import ConsumerProfileTestCase


class TestConsumerDetailsView(ConsumerProfileTestCase):
    def test__getConsumerDetails_withoutLoggedUser_shouldRedirectToLoginView(self):

        response = self.client.get(reverse('consumer detail'))

        self.assertEqual(302, response.status_code)

    def test__getConsumerDetails_withLoggedUser_shouldRedirectToConsumerDetails(self):
        self.client.force_login(self.user)
        profile = ConsumerUserProfile.objects.get(user_id=self.user.id)
        profile.name = 'Boyan'

        response = self.client.get(reverse('consumer detail'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['consumer'], profile)