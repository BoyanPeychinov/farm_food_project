from django.urls import reverse

from tests.base.tests import ProducerProfileTestCase


class TestListProducersProfilesView(ProducerProfileTestCase):
    def test__listedProducerProfiles_withCreatedProfile_shouldHaveOneProfile(self):
        response = self.client.get(reverse('list producers'))

        producers = list(response.context_data['producers'])

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(producers))