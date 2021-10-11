from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from car.api.v1.serializers import CarSerializer, CarRefuelSerializer, CarTripSerializer
from car.decorators import refuel_validator, trip_validator
from car.models import CarModel
from drf_yasg.utils import swagger_auto_schema


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

    @action(detail=True, methods=["post"])
    @trip_validator
    @swagger_auto_schema(request_body=CarTripSerializer, responses={200: CarSerializer})
    def trip(self, request, pk=None):
        return Response(data={})

    @action(detail=True, methods=["post"])
    @refuel_validator
    @swagger_auto_schema(
        request_body=CarRefuelSerializer, responses={200: CarSerializer}
    )
    def refuel(self, request, pk=None):
        car = self.get_object()

        return Response(data={})

    # @action(detail=True, methods=['post'])
    # def create_tyre(self):
    #     pass
