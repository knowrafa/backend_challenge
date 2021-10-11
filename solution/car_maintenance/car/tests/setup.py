from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status

from car.models import CarModel


class TestDefaultSetup(TestCase):
    def create_user(self):
        self.user = User.objects.create(username="test")
        self.user.set_password("test")
        self.user.save()

    def login_user(self):
        from rest_framework.test import APIClient

        self.client = APIClient()
        self.client.login(username="test", password="test")
