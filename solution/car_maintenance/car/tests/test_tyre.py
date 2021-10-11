from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status

from car.models import CarModel, TyreModel
from car.tests.setup import TestDefaultSetup


class TestTyre(TestDefaultSetup):
    def setUp(self):
        self.create_user()
        self.login_user()
        self.car_payload = {
            "name": "Test Car",
            "gas_capacity": 150,
        }
        self.car = CarModel.objects.create(**self.car_payload)
        self.car.save()
        self.tyres = []

        self.tyre_payload = {
            "car": self.car.pk,
        }
        for x in range(0, 3):
            self.tyres.append(TyreModel.objects.create(car=self.car))

    def test_post_tyre(self):
        request = self.client.post("/api/v1/tyres/", data=self.tyre_payload)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_car(self):
        request = self.client.get("/api/v1/tyres/")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve_car(self):
        request = self.client.get(f"/api/v1/tyres/{self.tyres[0].pk}/")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update_tyre(self):
        request = self.client.patch(
            f"/api/v1/tyres/{self.tyres[0].pk}/", data={"in_use": False}
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)
