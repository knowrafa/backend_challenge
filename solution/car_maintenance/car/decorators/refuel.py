from functools import wraps

from rest_framework.exceptions import ValidationError


def refuel_validator(func):
    """
    Decorator that raises a error when the car cannot be refuelled
    """

    @wraps(func)
    def decorator(self, request, **kwargs):
        car = self.get_object()
        if not car.can_refuel:
            raise ValidationError({
                "invalid": f"The car should NOT be refueled before it has less than"
                           f" {car.ACCEPTED_FOR_REFUEL}% gas on tank!"
            })
        return func(self, request, **kwargs)

    return decorator
