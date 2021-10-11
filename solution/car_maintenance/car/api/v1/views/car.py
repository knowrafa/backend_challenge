from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from car.api.v1.serializers import (
    CarSerializer,
    CarRefuelSerializer,
    CarTripSerializer,
    TyreSerializer,
)
from car.decorators import refuel_validator, trip_validator
from car.models import CarModel, TyreModel
from utils.serializers import create_update_object_serializer


class CarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = []

    @staticmethod
    def update_current_gas_count(car: CarModel, gas_count: float):
        create_update_object_serializer(
            Serializer_class=CarSerializer,
            instance=car,
            data={"gas_count": gas_count},
        )

    @staticmethod
    def calc_tyre_degradation(tyre: TyreModel, kilometers: float):
        """
        Calculate a single tyre degradation
        :param tyre: a TyreModel object
        :param kilometers: trip distance

        :return degradation after trip
        """
        return tyre.degradation + (kilometers / tyre.DEGRADATION_BY_KILOMETER)

    @staticmethod
    def calc_trip_gas_count(car: CarModel, kilometers: float):
        """
        Calculate a car consume based on trip distance
        :param car: a CarModel object
        :param kilometers: trip distance

        :return gas count after trip
        """

        return car.gas_count - (
            (kilometers / car.CONSUME_BY_LITER) * 100 / car.gas_capacity
        )

    @staticmethod
    def calc_refuel_gas_count(car: CarModel, liters: int):
        """
        Calculate new gas_count based on refuel liters
        :param car: a CarModel object
        :param liters: liters to refuel

        :return gas count after refuel
        """
        return car.gas_count + (liters * 100 / car.gas_capacity)

    def update_trip_tyre_degradation(
        self,
        car: CarModel,
        kilometers: float,
    ):
        """
        Update tyre degradation
        :param kilometers: trip distance
        :param car: Car instance to update the tyres
        """
        for tyre in car.tyres.filter(in_use=True):
            create_update_object_serializer(
                Serializer_class=TyreSerializer,
                instance=tyre,
                data={"degradation": self.calc_tyre_degradation(tyre, kilometers)},
            )

    def update_refuel_gas_count(self, car: CarModel, liters: int):
        self.update_current_gas_count(car, self.calc_refuel_gas_count(car, liters))

    def update_trip_gas_count(
        self,
        car: CarModel,
        kilometers: float,
    ):
        """
        Update gas_count
        :param kilometers: trip distance
        :param car: Car instance to be updated
        """
        self.update_current_gas_count(car, self.calc_trip_gas_count(car, kilometers))

    def perform_trip(self, car: CarModel, kilometers: float):
        self.update_trip_tyre_degradation(
            car,
            kilometers,
        )
        self.update_trip_gas_count(car, kilometers)

    def perform_refuel(self, car: CarModel, liters: int):
        self.update_refuel_gas_count(car, liters)

    @action(detail=True, methods=["post"])
    @trip_validator
    @swagger_auto_schema(request_body=CarTripSerializer, responses={200: CarSerializer})
    @transaction.atomic
    def trip(self, request, pk=None):
        self.perform_trip(
            self.get_object(),
            request.data.get("kilometers"),
        )
        return super(CarViewSet, self).retrieve(request)

    @action(detail=True, methods=["post"])
    @refuel_validator
    @swagger_auto_schema(
        request_body=CarRefuelSerializer,
        responses={200: CarSerializer},
    )
    @transaction.atomic
    def refuel(self, request, pk=None):
        self.perform_refuel(
            self.get_object(),
            request.data.get("liters"),
        )
        return super(CarViewSet, self).retrieve(request)
