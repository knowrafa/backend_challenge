from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from car.api.v1.serializers import (
    TyreSerializer,
    TyreSwapSerializer,
)
from car.decorators import swap_validator
from car.models import TyreModel
from utils.serializers import create_update_object_serializer


class TyreViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = TyreSerializer
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        car_pk = self.kwargs.get("car__pk")
        qs = TyreModel.objects.all()
        if car_pk:
            qs = TyreModel.objects.filter(car=car_pk)
        return qs.order_by('-in_use')

    @staticmethod
    def update_tyre_in_use(tyre: TyreModel, in_use):
        create_update_object_serializer(
            Serializer_class=TyreSerializer,
            instance=tyre,
            data={"in_use": in_use},
        )

    def perform_swap(self, tyre: TyreModel, new_tyre: TyreModel):
        self.update_tyre_in_use(tyre, False)
        self.update_tyre_in_use(new_tyre, True)

    @action(detail=True, methods=["post"])
    @swap_validator
    @swagger_auto_schema(
        request_body=TyreSwapSerializer,
        responses={200: TyreSerializer},
    )
    @transaction.atomic
    def swap(self, request, pk=None):
        """
        Method for swapping tyres
        Receives a pk tyre in params and pk tyre in request body.
        Evaluates if they can be swapped, then performs the swap
        :param request: Request
        :param pk: Tyre to be swapped
        """
        new_tyre = self.get_queryset().get(pk=request.data.get("tyre"))
        self.perform_swap(self.get_object(), new_tyre)
        return Response(data=TyreSerializer(instance=new_tyre).data)
