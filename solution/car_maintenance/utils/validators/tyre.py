from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class MaxDegradationValidator(BaseValidator):
    message = _(
        "Your degradation cannot be greater than %(limit_value)s. Change your tyres or take a shorter trip. "
    )
    code = "max_degradation"

    def compare(self, a, b):
        return a > b
