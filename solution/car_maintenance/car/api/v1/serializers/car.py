from action_serializer.serializers import ModelActionSerializer
from django.core.validators import MinValueValidator
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from car.api.v1.serializers import TyreSerializer
from car.models import CarModel, TyreModel
from utils.serializers import create_object_serializer


class CarSerializer(ModelActionSerializer):
    tyres = TyreSerializer(many=True, required=False)

    class Meta:
        model = CarModel
        fields = (
            "id",
            "name",
            "manufacturer",
            "year",
            "price",
            "description",
            "gas_capacity",
            "gas_count",
            "tyres",
        )

    @transaction.atomic
    def create(self, validated_data):
        instance = super(CarSerializer, self).create(validated_data)

        for count in range(0, 4):
            create_object_serializer(
                TyreSerializer,
                data={
                    "car": instance.pk,
                    "in_use": True,
                },
            )
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        tyres = validated_data.pop("tyres", [])

        for tyre in tyres:
            if tyre.get("in_use", True):
                if not instance.can_create_in_use_tyre:
                    raise ValidationError(
                        {
                            "invalid": "You cannot create another tyre, this car is already with 4 in use",
                        }
                    )
            create_object_serializer(TyreSerializer, data={"car": instance.pk, **tyre})
        return super(CarSerializer, self).update(
            instance=instance, validated_data=validated_data
        )

    @transaction.atomic
    def perform_trip(self):
        pass


class CarRefuelSerializer(serializers.Serializer):
    liters = serializers.FloatField(validators=[MinValueValidator(0)])


class CarTripSerializer(serializers.Serializer):
    kilometers = serializers.IntegerField(validators=[MinValueValidator(0)])
