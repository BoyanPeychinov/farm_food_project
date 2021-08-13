import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()


class ProducerProfileTestCase(TestCase):
    user_email = 'test_user@abv.bg'
    user_password = 'dasd7as!><2bdsa12347a@4=}{'
    name = 'Gosho'

    def setUp(self):
        self.client = Client()

        self.client.post(reverse('sign up'), data={
            'email': self.user_email,
            'password1': self.user_password,
            'password2': 'dasd7as!><2bdsa12347a@4=}{',
            'user_type': 'is_producer',
            'name': self.name
        })

        self.user = UserModel.objects.get(email=self.user_email)


class ConsumerProfileTestCase(TestCase):
    user_email = 'test_user@abv.bg'
    user_password = 'dasd7as!><2bdsa12347a@4=}{'
    name = 'Gosho'

    def setUp(self):
        self.client = Client()

        self.client.post(reverse('sign up'), data={
            'email': self.user_email,
            'password1': self.user_password,
            'password2': 'dasd7as!><2bdsa12347a@4=}{',
            'user_type': 'is_customer',
            'name': self.name
        })

        self.user = UserModel.objects.get(email=self.user_email)