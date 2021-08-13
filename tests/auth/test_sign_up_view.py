from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()


class SignUpViewTests(TestCase):
    def test_getSignUpPageUrl_shouldReturnSignUpPage(self):
        response = self.client.get(reverse("sign up"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='auth/sign_up.html')

    def test_createUser__withRightCredentials_shouldCreateUser(self):
        user_for_sign_up ={
            'email': 'test_user@abv.bg',
            'password1': 'dasd7as!><2bdsa12347a@4=}{',
            'password2': 'dasd7as!><2bdsa12347a@4=}{',
            'user_type': 'is_producer',
            'name': 'Gosho',
        }

        response = self.client.post(reverse('sign up'), data=user_for_sign_up)

        self.assertEqual(302, response.status_code)
        self.assertEqual(1, len(UserModel.objects.all()))

    def test_createUser__withWrongCredentials_shouldNotCreateUser(self):
        user_for_sign_up = {
            'email': 'test_user',
            'password1': 'dasd7as!><2bdsa12347a@4=}{',
            'password2': 'dasd7as!><2bdsa12347a@4=}{',
            'user_type': 'is_producer',
            'name': 'Gosho',
        }

        response = self.client.post(reverse('sign up'), data=user_for_sign_up)

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(UserModel.objects.all()))