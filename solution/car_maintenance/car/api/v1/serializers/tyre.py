from action_serializer.serializers import ModelActionSerializer
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from utils.validators.car import validate_in_use_tyre
from car.models import TyreModel


class TyreSerializer(ModelActionSerializer):
    class Meta:
        model = TyreModel
        fields = (
            "id",
            "car",
            "degradation",
            "in_use",
        )

    @transaction.atomic
    def create(self, validated_data):
        car = validated_data.get("car")
        if validated_data.get("in_use", False):
            validate_in_use_tyre(car)
        return super(TyreSerializer, self).create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        if validated_data.get("in_use", False):
            validate_in_use_tyre(instance.car)
        return super(TyreSerializer, self).update(
            instance=instance, validated_data=validated_data
        )


class TyreSwapSerializer(serializers.Serializer):
    tyre = serializers.PrimaryKeyRelatedField(queryset=TyreModel.objects.all())
