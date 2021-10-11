from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class MaxGasCountValidator(BaseValidator):
    message = _(
        "Your degradation cannot be greater than %(limit_value)s %. Refuel your car or take a shorter trip."
    )
    code = "max_gas_count"

    def compare(self, a, b):
        return a > b


@deconstructible
class MinGasCountValidator(BaseValidator):
    message = _(
        "You gas count cannot be lower than %(limit_value)s %. Refuel your car or take a shorter trip."
    )
    code = "min_gas_count"

    def compare(self, a, b):
        return a < b
