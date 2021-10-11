from functools import wraps

from rest_framework.exceptions import ValidationError


def trip_validator(func):
    @wraps(func)
    def decorator(self, request, **kwargs):
        car = self.get_object()
        if not car.can_trip:
            raise ValidationError({
                "invalid": "The car cannot start a trip with no gas or less than 4 tyres in use!"
            })
        return func(self, request, **kwargs)

    return decorator
