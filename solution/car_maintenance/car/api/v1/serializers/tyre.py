from action_serializer.serializers import ModelActionSerializer

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
        action_fields = {
            "create": {
                "fields": (
                    "id",
                    "car",
                    "degradation",
                    "in_use",
                )
            },
            "list": {
                "fields": (
                    "id",
                    "degradation",
                    "in_use",
                )
            },
            "update": {
                "fields": (
                    "id",
                    "degradation",
                    "in_use",
                )
            },
            "partial_update": {
                "fields": (
                    "id",
                    "degradation",
                    "in_use",
                )
            },
        }
