import datetime

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()


class SignInViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test_user@abv.bg',
            password='dasd7as!><2bdsa12347a@4=}{',
            is_staff=False,
            date_joined=datetime.datetime.now(),
            is_producer=True,
            is_consumer=False,
        )

    def test_getSignInPageUrl_shouldReturnSignInPage(self):
        response = self.client.get(reverse("sign in"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='auth/sign_in.html')

    def test_loginUser__withRightCredentials_shouldLogInUser(self):
        logged_in = self.client.login(username="test_user@abv.bg", password='dasd7as!><2bdsa12347a@4=}{')

        self.assertTrue(logged_in)

    def test_loginUser__withWrongCredentials_shouldNotLogInUser(self):
        not_logged_in = self.client.login(username="wrong_user", password='wrong_pass')

        self.assertFalse(not_logged_in)