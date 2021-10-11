from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


def validate_in_use_tyre(car):
    if not car.can_create_in_use_tyre:
        raise ValidationError(
            {
                "invalid": "You cannot create another tyre, this car is already with 4 in use",
            }
        )


@deconstructible
class MaxGasCountValidator(BaseValidator):
    message = _(
        "Your gas count cant be cannot be greater than %(limit_value)s. Refuel your car or take a shorter trip."
    )
    code = "max_gas_count"

    def compare(self, a, b):
        return a > b


@deconstructible
class MinGasCountValidator(BaseValidator):
    message = _(
        "You gas count cant be lower than %(limit_value)s. Refuel your car or take a shorter trip."
    )
    code = "min_gas_count"

    def compare(self, a, b):
        return a < b
