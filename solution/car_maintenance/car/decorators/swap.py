from functools import wraps

from rest_framework.exceptions import ValidationError

from car.models import TyreModel


def swap_validator(func):
    @wraps(func)
    def decorator(self, request, **kwargs):
        tyre = self.get_object()
        try:
            new_tyre = TyreModel.objects.get(pk=request.data.get("tyre"))
        except TyreModel.DoesNotExist:
            raise ValidationError({"invalid": f"This tyre does not exist"})
        if not tyre.can_be_swapped and tyre.in_use:
            raise ValidationError(
                {
                    "invalid": f"This tyres cannot be swapped."
                    f" Assure that tyre is in use and"
                    f" he has more than {tyre.TYRE_DEGRADATION_FOR_CHANGE}% of degradation."
                }
            )
        elif tyre.car != new_tyre.car:
            raise ValidationError(
                {
                    "invalid": f"Both tyres should be from same car. "
                    f"Choose only same car tyres."
                }
            )
        return func(self, request, **kwargs)

    return decorator
