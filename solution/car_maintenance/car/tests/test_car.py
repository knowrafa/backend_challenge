from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status

from car.models import CarModel
from car.tests.setup import TestDefaultSetup


class TestCar(TestDefaultSetup):
    def setUp(self):
        self.create_user()
        self.login_user()
        self.payload = {
            "name": "Test Car",
            "gas_capacity": 150,
        }
        self.car = CarModel.objects.create(**self.payload)
        self.car.save()

    def test_post_car(self):
        request = self.client.post("/api/v1/cars/", data=self.payload)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_car(self):
        request = self.client.get("/api/v1/cars/")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve_car(self):
        request = self.client.get(f"/api/v1/cars/{self.car.pk}/")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update_car(self):
        request = self.client.patch(
            f"/api/v1/cars/{self.car.pk}/", data={"tyres": [{"in_use": True}]}
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        request = self.client.patch(
            f"/api/v1/cars/{self.car.pk}/", data={"tyres": [{"in_use": False}]}
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        request = self.client.patch(
            f"/api/v1/cars/{self.car.pk}/", data={"name": "Test Car 2"}
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data.get("name"), "Test Car 2")
