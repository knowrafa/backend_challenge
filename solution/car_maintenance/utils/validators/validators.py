from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PorcentagemValidator:
    def __call__(self, gas_count):
        try:
            if not (0 <= gas_count <= 100):
                raise ValidationError(
                    f"{gas_count} should be between 0 and 100", params={"gas_count": gas_count}
                )
        except TypeError:
            raise ValidationError(
                f"{gas_count} should be a number", params={"gas_count": gas_count}
            )


