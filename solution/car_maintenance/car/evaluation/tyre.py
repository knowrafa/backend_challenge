from django.core.exceptions import ValidationError


def verify_max_active_tyres(tyre):
    if tyre.is_active and tyre.car.tyres.exclude(pk=tyre.pk).filter(active=True).count() == 4:
        raise ValidationError({
            "invalid": "This car already have 4 active tyres",
        })
